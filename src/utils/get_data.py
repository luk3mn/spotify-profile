import requests


class GetData:
    """To be able to extract private data from Spotify Account"""

    def __init__(self, headers: object) -> object:
        """
        :param headers (object): to set the headers that it will be used
        """
        self.__endpoint = "https://api.spotify.com/v1"
        self.__headers = headers

    def get_users_top_items(self, limit: int = 25, offset: int = 0, type_item: str = 'tracks', time_range: str = 'medium_term') -> object:
        """Get user's top items of the type 'tracks' from Spotify API

        :param limit (int): The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
        :param offset (int): The index of the first item to return. Default: 0 (the first item). Use with limit to get the next set of items.
        :param type_item (int): The type of entity to return, artists or tracks. Default: 'tracks'
        :param time_range: there are three option based on API instructions, they are short_term (about 4 weeks), 
         medium_term (approximately last 6 months) and long_term (calculated from several years of data and including all new data as it becomes available)
        :return response (json): json response 
        """
        response = requests.get(url=f'{self.__endpoint}/me/top/{type_item}?limit={limit}&offset={offset}&time_range={time_range}', headers=self.__headers, timeout=5)

        return response.json()

    def get_users_profile(self, user_id: str):
        """
        :param user_id (str): spotify's username
        :return response (json): api spotify user's profile request
        """
        response = requests.get(url=f"{self.__endpoint}/users/{user_id}", headers=self.__headers, timeout=5)
        return response.json()

    def get_current_users_playlist(self, limit: int = 25, offset: int = 0):
        """
        :param limit (int): playlist limit number
        :param offset (int): The index of the first playlist to return
        :return response (json): current playlist response 
        """
        response = requests.get(url=f"{self.__endpoint}/me/playlists?limit={limit}&offset={offset}", headers=self.__headers, timeout=5)
        return response.json()

    def get_recently_played_tracks(self, limit: int = 25):
        """
        :param limit (int): the maximum number of items to return
        """
        response = requests.get(url=f"{self.__endpoint}/me/player/recently-played?limit={limit}", headers=self.__headers, timeout=5)
        return response.json()

    def search_for_item(self, q: str = "rock", search_type: str = "playlist", limit: int = 25, offset: int = 0):
        """
        :param q (str): Your search query
        :param search_type (str): list of item types to search across "album", "artist", "playlist", "track", "show", "episode", "audiobook"
        :param limit (int): The maximum number of results to return in each item type
        :param offset (int): The index of the first result to return
        """
        response = requests.get(url=f"{self.__endpoint}/search?q={q}&type={search_type}&limit={limit}&offset={offset}", headers=self.__headers, timeout=3)
        return response.json()

    # def get_users_saved_tracks(self):
    #     collection = []
    #     for i in range(1, 852, 50):
    #         response = requests.get(url=f"{self.__endpoint}me/tracks?limit=50&offset={i}", headers=self.__headers, timeout=2)
    #         print("Waiting...", i)
    #         collection.append(response.json())
    #     return collection
