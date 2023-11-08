import pandas as pd

class DataFormat:
    """ This module refers to data organization after extracting from Spotify API:
        - These data are stored in a json file
        - We can run this json file and get just values important for us
        - Finally, we will be able to structure these data in pandas DataFrame before loading it in some database
    """
    def __init__(self, response) -> None:
        """ Structuring data collection 
        
        :param response (json): json response
        """
        self.response = response

    def format_top_items(self) -> object:
        """
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
        for r in self.response['items']:
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
            # print(r['album']['images'][0]['url'])

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
    
    def get_tracks_uris(self) -> list:
        """ Get uris from json file
        
        :return (uris): uris Spotify tracks list
        """
        uris = []

        for r in self.response['items']:
            uris.append(r['uri'])
            
        return uris
    