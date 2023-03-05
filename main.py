import os

from googleapiclient.discovery import build
from utils.ychannel import Ychannel
from utils.video import Video, PLVideo
from utils.playlist import PlayList



vdud = Ychannel('UCMCgOm8GZkHp8zJ6l7_hIuA')
red = Ychannel('UC1eFXmJNkjITxPFWTy6RsWg')

video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.playlist_name)
print(pl.url)
print(pl.playlist_dict2())