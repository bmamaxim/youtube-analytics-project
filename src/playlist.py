import os
from datetime import timedelta
import isodate

from googleapiclient.discovery import build

from src.video import Video


class PlayList:
    api_key: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        #self.playlists = self.get_service().playlists().list(channelId=channel_id,
                                                             #part='contentDetails,snippet',
                                                             #maxResults=50, ).execute()
        # self.title = self.playlists['items'][0]['snippet']['title']
        # self.playlist_videos = self.get_service().playlistItems().list(playlistId=self._id,
        # part='contentDetails',
        # maxResults=50).execute()
        # self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        # self.videos = [Video(video_id) for video_id in self.video_ids]
        # self.url = self.get_service()

    @classmethod
    def get_service(cls):
        """
        Функция принимает API_KEY строит путь до данных по API_KEY
        возвращает путь
        """
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def total_duration(self):
        """
        Возвращает объект класса `datetime.timedelta` с суммарной длительностью плейлиста
        """
        playlist_duration = timedelta(seconds=0)
        for video in self.videos:
            playlist_duration += isodate.parse_duration(video.duration)
        return playlist_duration

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        return max(self.videos, key=lambda i: i.likes_count)


channel_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

playlists = youtube.playlists().list(channelId=channel_id,
                                     part='contentDetails,snippet',
                                     maxResults=50,
                                     ).execute()
print(api_key)
print(youtube.playlists().list(channel_id))
#print(playlists)
