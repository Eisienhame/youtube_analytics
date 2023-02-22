import os

from googleapiclient.discovery import build
from utils import Ychannel



vdud = Ychannel('UCMCgOm8GZkHp8zJ6l7_hIuA')
red = Ychannel('UC1eFXmJNkjITxPFWTy6RsWg')
print(vdud.title)
print(vdud.videocount)
print(vdud.url)

print(Ychannel.get_service())

print(vdud > red)