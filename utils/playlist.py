import json, os, datetime
from googleapiclient.discovery import build

class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist_name = self.playlist_dict()['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    def __repr__(self):
        return f'({self.playlist_name})'


    @classmethod
    def get_service(cls):
        "Создать специальный объект для работы с API"

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def playlist_dict(self):
        "Создается словарь с информацией о Ютуб playlist взятый из обьекта для работы с API"
        youtube = PlayList.get_service()
        playlist = youtube.playlists().list(id=self.__playlist_id, part='snippet').execute()
        return playlist

    def playlist_dict2(self):
        "Создается словарь с информацией о Ютуб playlist взятый из обьекта для работы с API"
        youtube = PlayList.get_service()
        playlist = youtube.playlists().list(id=self.__playlist_id, part='data').execute()
        return playlist

    @property
    def total_duration(self):
        pass