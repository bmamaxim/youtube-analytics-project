import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')

    def __init__(self, video_id: str):
        self.video_id = video_id
        try:
            self.video_response = self.get_service().videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=self.video_id
                ).execute()
            self.title: str = self.video_response()['items'][0]['snippet']['title']
            self.url: str = f'https://youtu.be/{self.video_id}'
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
            self.duration: str = self.video_response['items'][0]['contentDetails']['duration']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        except Exception:
            self.title: str = None
            self.url: str = None
            self.view_count: int = None
            self.comment_count: int = None
            self.duration: str = None
            self.like_count: int = None

    @classmethod
    def get_service(cls):
        """
        Функция принимает API_KEY строит путь до данных по API_KEY
        возвращает путь
        """
        return build('youtube', 'v3', developerKey=cls.api_key)

    def __str__(self) -> str:
        return self.title


class PLVideo(Video):
    """
    Класс наследник:
    второй класс для видео `PLVideo`, который инициализируется  'id видео' и 'id плейлиста
    """

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
