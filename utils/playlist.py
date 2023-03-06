import json, os, datetime, isodate
from googleapiclient.discovery import build
from utils.video import Video, PLVideo
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

    def playlist_videos(self):
        "Создается словарь с информацией о Ютуб видео в playlist взятый из обьекта для работы с API"
        youtube = PlayList.get_service()
        playlist = youtube.playlistItems().list(playlistId=self.__playlist_id, part='contentDetails').execute()
        return playlist

    @property
    def total_duration(self):
        'Получаем суммарное время видео из плейлиста'
        youtube = PlayList.get_service()
        video_ids = []
        for i in self.playlist_videos()['items']:
            video_ids.append(i['contentDetails']['videoId'])

        response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()

        total_duration = datetime.timedelta()

        for i in response['items']:
            iso_duration = i['contentDetails']['duration']
            duration = isodate.parse_duration(iso_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        best_id = ''
        best_likes = 0
        for i in self.playlist_videos()['items']:
            next_video = Video(i['contentDetails']['videoId'])
            if int(next_video.likes_count) > best_likes:
                best_likes = int(next_video.likes_count)
                best_id = i['contentDetails']['videoId']
        link = 'https://youtu.be/' + best_id
        print(link)
