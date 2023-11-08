"""
### Player (screen)
- Get Recently Played Tracks

### Playlist (Screen)
- Get User's Playlists

### Tracks
- Get User's Saved Tracks
- Get Recommendations


### Users
- Get Current User's Profile
- Get User's Top Items (preview_url, external_urls[spotify]:'artist' and 'track'; url[track_image] )
    - Tracks
    - Artists
- Get Followed Artists



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
from flask import render_template, redirect, session, request
from dotenv import load_dotenv
import os

load_dotenv()

from config import create_app
from track import TrackController, TrackModel
from utils import GetData, Authorization, DataFormat



SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_USER_ID = os.getenv('USER_ID')

### URL APIs
TOKEN_URL = 'https://accounts.spotify.com/api/token'
ENDPOINT = 'https://api.spotify.com/v1/'
REDIRECT_URI = os.getenv("REDIRECT_URI")

get_authorization = Authorization(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, token_url=TOKEN_URL)

app = create_app()
# track_c = TrackController()

@app.route('/')
def profile():
    return render_template('profile.html')

@app.route('/authorization')
def authorization():
    auth_url = get_authorization.get_auth(scope='user-top-read playlist-modify-public playlist-modify-private')
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

        get_data = GetData(endpoint=ENDPOINT, headers=headers)
        response = get_data.get_users_top_items(time_range='short_term', filename='short_term.json', limit=50)
        
        data_format = DataFormat(response=response)
        
        track_c = TrackController()
        track_c.insert_data(data_format.format_top_items())
    except:
        return redirect('/authorization') # if access token doesn't exist, redirect to get a new authentication

    return redirect('/')

@app.route('/tracks')
def tracks():
    try:
        track_c = TrackController()
        tracks = track_c.retrieve_data()
        return render_template('tracks.html', tracks=tracks)
    except:
        return redirect('/authorization')

@app.route('/playlists')
def playlist():
    return render_template('playlists.html')

if __name__ == "__main__":
    app.run(debug=True)