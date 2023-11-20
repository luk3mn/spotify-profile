import pandas as pd

class DataFormat:
    """ This module refers to data organization after extracting from Spotify API:
        - These data are stored in a json file
        - We can run this json file and get just values important for us
        - Finally, we will be able to structure these data in pandas DataFrame before loading it in some database
    """
    def __init__(self) -> None:
        """ Structuring data collection 
        """

    def format_top_items(self, response: object) -> object:
        """
        :param response (object): json response
        :return df (DataFrame): return to web app a pandas frame work
        """
        song_names = []
        song_id = []
        artist_names = []
        album_name = []
        release_date = []
        popularity = []
        preview_url = []
        images_url = []
        spotify_song = []
        spotify_album = []
        spotify_artist = []

        ### Storing our data into lists
        for r in response['items']:
            song_names.append(r['name'])
            song_id.append(r['id'])
            artist_names.append(r['artists'][0]['name'])
            album_name.append(r['album']['name'])
            release_date.append(r['album']['release_date'])
            popularity.append(r['popularity'])
            preview_url.append(r['preview_url'])
            images_url.append(r['album']['images'][0]['url'])
            spotify_song.append(r['external_urls']['spotify'])
            spotify_artist.append(r['artists'][0]['external_urls']['spotify'])
            spotify_album.append(r['album']['external_urls']['spotify'])

        ### Dictionary to structure our data before transforming in pandas DataFrame
        song_dict = {
            'song_id': song_id,
            'song': song_names,
            'artist': artist_names,
            'album': album_name,
            'release': release_date,
            'popularity': popularity,
            'preview_url': preview_url,
            'images_url': images_url,
            'spotify_song': spotify_song,
            'spotify_artist':spotify_artist,
            'spotify_album':spotify_album
        }

        ### Here we could structured our data in pandas and returned as a object
        df = pd.DataFrame(song_dict, columns=['song_id', 'song', 'artist', 'album', 'release', 'popularity', 'preview_url', 'images_url', 'spotify_song', 'spotify_artist', 'spotify_album'])
        return df

    def format_users_profile(self, response: object) -> object:
        """
        :param response (object): json response from user's profile
        :return df (DataFrame): pandas DataFrame with data requests
        """

        profile_dict = {
            "name": [response['display_name']],
            "profile": [response['images'][1]['url']],
            "spotify_profile": [response['external_urls']['spotify']],
            "spotify_id": [response['id']]
        }

        return pd.DataFrame(profile_dict)

    def format_top_artists(self, response: object) -> object:
        """
        :param response (object): json response from followed artist
        :return df (DataFrame): pandas DataFrame with data requests
        """

        artist_id = []
        artist = []
        genres = []
        followers = []
        popularity = []
        images_artist = []
        spotify_url = []

        for r in response['items']:
            artist_id.append(r['id'])
            artist.append(r['name'])
            genres.append(', '.join(str(g) for g in r['genres']))
            followers.append(r['followers']['total'])
            popularity.append(r['popularity'])
            images_artist.append(r['images'][0]['url'])
            spotify_url.append(r['external_urls']['spotify'])

        dict_artist = {
            "id": artist_id,
            "artist": artist,
            "genres": genres,
            "popularity": popularity,
            "image_artist": images_artist,
            "spotify_url": spotify_url 
        }

        return pd.DataFrame(dict_artist)
