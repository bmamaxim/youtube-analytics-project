import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.video_title = self.video_response()['items'][0]['snippet']['title']
        self.url = f"https://youtu.be/{self.video_id}"
        self.view_count = self.video_response()['items'][0]['statistics']['viewCount']
        self.comment_count = self.video_response()['items'][0]['statistics']['commentCount']
        self.duration = self.video_response()['items'][0]['contentDetails']['duration']

    @classmethod
    def get_service(cls):
        """
        Функция принимает API_KEY строит путь до данных по API_KEY
        возвращает путь
        """
        return build('youtube', 'v3', developerKey=cls.api_key)

    def video_response(self):
        """
        Метод получит статистику видео по его id
        """
        return self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()

    def __str__(self) -> str:
        return self.video_title


class PLVideo(Video):
    """
    Класс наследник:
    второй класс для видео `PLVideo`, который инициализируется  'id видео' и 'id плейлиста
    """

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
