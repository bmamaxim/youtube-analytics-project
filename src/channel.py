import json
import os
from typing import List, Any

from googleapiclient.discovery import build

#import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber = channel['items'][-1]['statistics']['subscriberCount']
        self.video_count = channel['items'][-1]['statistics']['videoCount']
        self.views = channel['items'][-1]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.__channel_id)

    @classmethod
    def get_service(cls):
        """
        Функция принимает API_KEY строит путь до данных по API_KEY
        возвращает путь
        """
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, file_name):
        """
        Записывает словарь в json-подобном удобном формате с отступами
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            result = {
                'id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber': self.subscriber,
                'video_count': self.video_count,
                'views': self.views,
            }
            json.dump(result, file, indent=2, ensure_ascii=False)

    def __add__(self, other):
        """
        Метод суммирует подписчиков ютуб каналов
        """
        return int(self.subscriber) + int(other.subscriber)

    def __sub__(self, other):
        """
        Метод врзвращает разницу подписчиков ютуб каналов
        """
        return int(self.subscriber) - int(other.subscriber)

    def __lt__(self, other):
        """
        Метод сравнения: возвращает True если 'меньше' подписчиков ютуб каналов
        """
        return int(self.subscriber) < int(other.subscriber)

    def __le__(self, other):
        """
        Метод сравнения: возвращает True если 'меньше или равно' подписчиков ютуб каналов
        """
        return int(self.subscriber) <= int(other.subscriber)

    def __gt__(self, other):
        """
        Метод сравнения: возвращает True если 'больше' по подписчикам ютуб каналов
        """
        return int(self.subscriber) > int(other.subscriber)

    def __ge__(self, other):
        """
        Метод сравнения: возвращает True если 'больше или равно' по подписчикам ютуб каналов
        """
        return int(self.subscriber) >= int(other.subscriber)

    def __str__(self):
        return f"{self.title} {self.url}"

