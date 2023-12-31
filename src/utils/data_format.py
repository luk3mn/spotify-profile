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

    def format_top_tracks(self, response: object) -> pd.DataFrame:
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

    def format_users_profile(self, response: object) -> pd.DataFrame:
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

    def format_top_artists(self, response: object) -> pd.DataFrame:
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

    def format_current_playlists(self, response: object) -> pd.DataFrame:
        """
        :param response (object): playlist response
        :return DataFrame (object): Playlist pandas DataFrame
        """
        id_playlist = []
        image = []
        name = []
        owner = []
        total = []
        spotify_url = []

        for r in response['items']:
            id_playlist.append(r['id'])
            name.append(r['name'])
            image.append(r['images'][0]['url'])
            owner.append(r['owner']['display_name'])
            total.append(r['tracks']['total'])
            spotify_url.append(r['external_urls']['spotify'])

        dict_playlists = {
            "id": id_playlist,
            "name":name,
            "image":image,
            "owner":owner,
            "total":total,
            "spotify_url":spotify_url
        }

        df = pd.DataFrame(dict_playlists)
        return df

    def format_recently_played_tracks(self, response: object) -> pd.DataFrame:
        """
        :param response (object): Spotify API response
        :return DataFrame (object): pandas DataFrame object
        """

        played_at = []
        name = []
        track_id = []
        image = []
        artist = []
        album = []
        release = []
        album_url = []
        popularity = []
        preview_url = []
        spotify_url = []

        for r in response['items']:
            played_at.append(r['played_at'])
            name.append(r['track']['name'])
            track_id.append(r['track']['id'])
            artist.append(r['track']['artists'][0]['name'])
            album.append(r['track']['album']['name'])
            release.append(r['track']['album']['release_date'])
            popularity.append(r['track']['popularity'])
            preview_url.append(r['track']['preview_url'])
            spotify_url.append(r['track']['external_urls']['spotify'])
            album_url.append(r['track']['album']['external_urls']['spotify'])
            image.append(r['track']['album']['images'][0]['url'])

        dict_played = {
            "played_at": played_at,
            "name": name,
            "image": image,
            "track_id": track_id,
            "artist": artist,
            "album": album,
            "release": release,
            "popularity": popularity,
            "preview_url": preview_url,
            "spotify_url": spotify_url,
            "album_url": album_url
        }

        return pd.DataFrame(dict_played)

    def format_search_for_item(self, response: object) -> pd.DataFrame:
        """
        :param response (object): json response API
        :return DataFrame (object): pandas DataFrame object
        """
        name = []
        item_id = []
        image = []
        total = []
        owner = []
        spotify_url = []

        for r in response['playlists']['items']:
            if r['owner']['display_name'] == "Spotify":
                item_id.append(r['id'])
                name.append(r['name'])
                image.append(r['images'][0]['url'])
                total.append(r['tracks']['total'])
                spotify_url.append(r['external_urls']['spotify'])
                owner.append(r['owner']['display_name'])

        dict_items = {
            "id": item_id,
            "name": name,
            "image": image,
            "total": total,
            "owner": owner,
            "spotify_url": spotify_url
        }

        return pd.DataFrame(dict_items)
