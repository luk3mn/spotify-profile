"""
### Playing (screen)
- Discovery Weekly
- Get Recently Played Tracks
    - Last 7 Days or Tops Tacks this month
    - Last Track Played
    - Get Recommendations
        - Preview Tracks (show just tracks with preview_url and random way)
        - Search for Item (Playlist, Artist or Track)
- Get User's Saved Albums
- Get User's Saved Tracks (limit, offset)
- Get User's Top Items (type: "track", "long_term") -> 50 items

### Profile (Screen)
- Get Current User's Profile
- Get User's Top Items (type: "artist")
- Get User's Playlists

### Tracks
- Get User's Top Items (type: "track") -> 50 items


1. Show my spotify data to anyone (Back-end)
    a. Extract my Spotify data
    b. Transform my spotify data
    c. Load my Spotify data
    d. Fetch my Spotify data on data database show up to user's on front end
2. Allow uses to verify your own data (Front-end)
    - it'll be necessary add these users as testers
    - if these users don't be add, they can see just my Spotify data on front-end using a database
    - When these users are allow to see their own Spotify data, the app show up these data directly from spotify API request (not database)

NOTE: the application store just my Spotify data, the used as data sample of application
NOTE: We explore the options to store links related with our Spotify data de create an interactive experience with other users, even if they wasn't
      on web app
"""
import os
from flask import Flask, render_template, redirect, session, request
from dotenv import load_dotenv

from .utils import GetData, Authorization, DataFormat
from .application.controller import ApplicationController
from .application.recently_played_controller import RecentlyPlayedController
from .application.modals import TrackModel, ProfileModel, ArtistModel, PlaylistModel, DiscoverWeeklyModel, RecommendationModel, RecentlyPlayedModel
from .ext import configuration, database

load_dotenv()



SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_USER_ID = os.getenv('USER_ID')

### URL APIs
TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = os.getenv("REDIRECT_URI")

get_authorization = Authorization(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, token_url=TOKEN_URL)

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)

@app.route('/')
def profile():
    artists = ApplicationController(model=ArtistModel()).retrieve_data()
    user_profile = ApplicationController(model=ProfileModel()).retrieve_data()
    playlists = ApplicationController(model=PlaylistModel()).retrieve_data()
    return render_template('profile.html', artists=artists, user_profile=user_profile, playlists=playlists)

@app.route('/authorization')
def authorization():
    auth_url = get_authorization.get_auth(scope='user-top-read playlist-modify-public playlist-modify-private playlist-read-private user-read-recently-played user-library-read')
    return redirect(auth_url)

@app.route('/callback')
def callback():

    try:
        session.clear()
        code = request.args['code']
        session['access_token'] = get_authorization.get_token(code=code).json()['access_token']

        headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/json",
            "Authorization" : "Bearer {token}".format(token=session['access_token'])
        }

        get_data = GetData(headers=headers)
        data_format = DataFormat()

    except Exception:
        return redirect('/authorization') # if access token doesn't exist, redirect to get a new authentication

    track_c = ApplicationController(model=TrackModel())
    track_c.insert_data(data_format.format_top_tracks(response=get_data.get_users_top_items(time_range='medium_term', limit=50)))

    profile_c = ApplicationController(model=ProfileModel())
    profile_c.insert_data(data_format.format_users_profile(response=get_data.get_users_profile(user_id=SPOTIFY_USER_ID)))

    artists_c = ApplicationController(model=ArtistModel())
    artists_c.insert_data(data_format.format_top_artists(response=get_data.get_users_top_items(type_item='artists', limit=50)))

    playlist_c = ApplicationController(model=PlaylistModel())
    playlist_c.insert_data(data_format.format_current_playlists(response=get_data.get_current_users_playlist(limit=50)))

    recently_played_c = ApplicationController(model=RecentlyPlayedModel())
    recently_played_c.insert_data(data_format.format_recently_played_tracks(get_data.get_recently_played_tracks(limit=50)))

    recommendation_c = ApplicationController(model=RecommendationModel())
    recommendation_c.insert_data(data_format.format_search_for_item(response=get_data.search_for_item(q='rock', limit=20)))

    discover_c = ApplicationController(model=DiscoverWeeklyModel())
    discover_c.insert_data(data_format.format_search_for_item(response=get_data.search_for_item(q='discover weekly', limit=1)))
    return redirect('/')

@app.route('/tracks')
def tracks():
    try:
        track_c = ApplicationController(model=TrackModel())
        track_response = track_c.retrieve_data()
        return render_template('tracks.html', track_response=track_response)
    except Exception:
        return redirect('/authorization')

@app.route('/discover')
def discover():
    # access controller with SQL Query to recently played track
    recently_played_tracks = RecentlyPlayedController()

    recommendation = ApplicationController(model=RecommendationModel())
    spotify_discover = ApplicationController(model=DiscoverWeeklyModel())

    played_tracks = recently_played_tracks.group_by_track()
    most_played = recently_played_tracks.most_played_track()
    latest_played = recently_played_tracks.latest_played_track()

    recommendations = recommendation.retrieve_data()
    discover_weekly = spotify_discover.retrieve_data()
    return render_template('discover.html',
                           recommendations=recommendations,
                           discover_weekly=discover_weekly,
                           played_tracks=played_tracks,
                           most_played=most_played,
                           latest_played=latest_played)
