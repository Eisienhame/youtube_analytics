import json, os
from googleapiclient.discovery import build


class Ychannel:
    def __init__(self, id):
        self.__id = id

        self.title = self.channel_dict()['items'][0]['snippet']['title']
        self.description = self.channel_dict()['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + str(id)
        self.subscribers = self.channel_dict()['items'][0]['statistics']['subscriberCount']
        self.videocount = self.channel_dict()['items'][0]['statistics']['videoCount']
        self.viewcount = self.channel_dict()['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    @classmethod
    def __verify_data(cls, other):
        return other.subscribers
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.subscribers > sc
    def __add__(self, other):
        return int(self.subscribers) + int(other.subscribers)


    @classmethod
    def get_service(cls):
        "Создать специальный объект для работы с API"

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def id(self, id=None):
        "Делаем id не изменяемым"
        if id == None:
            return self.__id
        else:
            raise Exception("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    def channel_dict(self):
        "Создается словарь с информацией о Ютуб канале взятый из обьекта для работы с API"
        youtube = Ychannel.get_service()

        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        return channel

    def print_info(self):
        "Вывод инфы "

        channel = self.channel_dict()

        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, name:str):
        "Создаем json файл с основными параметрами ютуб канала"

        dict_for_json = {
            'title':self.title,
            'description':self.description,
            'url':self.url,
            'subscribers':self.subscribers,
            'videoCount':self.videocount,
            'viewcount':self.viewcount
  }

        with open(name, 'w', encoding='utf-8') as f:
            json.dump(dict_for_json, f, ensure_ascii=False, indent=4)