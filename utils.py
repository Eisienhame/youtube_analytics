import json

class Ychannel:
    def __init__(self, id):
        self.id = id


    def print_info(self):
        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))