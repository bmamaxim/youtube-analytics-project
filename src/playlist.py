import os
from datetime import timedelta
import isodate

from googleapiclient.discovery import build

from src.video import Video


class PlayList:
    api_key: str = os.getenv('API_KEY')

    def __init__(self, _id: str):
        self.playlist_id = _id
        self.playlist = self.get_service().playlists().list(id=self.playlist_id,
                                                            part='snippet',
                                                            maxResults=50).execute()
        self.title = self.playlist.get('items')[0]['snippet']['title']
        self.info_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                   part='contentDetails, snippet',
                                                                   maxResults=50).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.info_videos['items']]
        self.videos = [Video(video_id) for video_id in self.video_ids]
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"


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
        best_video: Video = max(self.videos, key=lambda i: i.like_count)
        return best_video.url

    def __repr__(self):
        return f"{self.url}"
