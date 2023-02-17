import os

from googleapiclient.discovery import build
from utils import Ychannel

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

vdud = Ychannel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()