import json, os
from googleapiclient.discovery import build

class Ychannel:
    def __init__(self, id):
        self.id = id


    def print_info(self):
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))

