import json, os
from googleapiclient.discovery import build



class Video:
    def __init__(self, video_id):
        self.__video_id = video_id
        self.video_name = self.video_dict(self.__video_id)['items'][0]['snippet']['title']
        self.view_count = self.video_dict(self.__video_id)['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_dict(self.__video_id)['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return self.video_name
    @classmethod
    def get_service(cls):
        "Создать специальный объект для работы с API"

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def video_dict(self, v_id):
        "Создается словарь с информацией о Ютуб video взятый из обьекта для работы с API, v_id йди нужен чтобы саблассы моли использовать"
        youtube = Video.get_service()

        video = youtube.videos().list(id=v_id, part='snippet,statistics').execute()
        return video

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        self.__video_id = video_id
        self.__playlist_id = playlist_id
        self.playlist_name = self.playlist_dict()['items'][0]['snippet']['title']
        self.video_name = self.video_dict(self.__video_id)['items'][0]['snippet']['title']
        self.view_count = self.video_dict(self.__video_id)['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_dict(self.__video_id)['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return f'{self.video_name} ({self.playlist_name})'
    def playlist_dict(self):
        "Создается словарь с информацией о Ютуб playlist взятый из обьекта для работы с API"
        youtube = PLVideo.get_service()
        playlist = youtube.playlists().list(id=self.__playlist_id, part='snippet').execute()
        return playlist