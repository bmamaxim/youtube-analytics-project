import json
import os
from typing import List, Any

from googleapiclient.discovery import build

#import isodate

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.get_service.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(channel)
        #self.title = title
        #self.description = description
        #self.url = url
        #self.subscriber = subscriber
        #self.video_count = video_count
        #self.views = views

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.__channel_id)

    @classmethod
    def get_service(cls):
        """
        Функция принимает API_KEY строит путь до данных по API_KEY
        возвращает путь до файла
        """
        return build('youtube', 'v3', developerKey=os.getenv('API_KEY'))

    def to_json(self, file_name):
        """
        Записывает словарь в json-подобном удобном формате с отступами
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dumps(file, indent=2, ensure_ascii=False)

    def __add__(self, other):
        """
        Метод сложения по подписчикам ютуб каналов
        """
        return self.subscriber + other.subscriber

    def __sub__(self, other):
        """
        Метод вычитания по подписчикам ютуб каналов
        """
        return self.subscriber - other.subscriber

    def __lt__(self, other):
        """
        Метод сравнения 'меньше' по подписчикам ютуб каналов
        """
        return self.subscriber < other.subscriber

    def __le__(self, other):
        """
        Метод сравнения 'меньше или равно' по подписчикам ютуб каналов
        """
        return self.subscriber <= other.subscriber

    def __gt__(self, other):
        """
        Метод сравнения больше по подписчикам ютуб каналов
        """
        return self.subscriber > other.subscriber

    def __ge__(self, other):
        """
        Метод сравнения 'больше или равно' по подписчикам ютуб каналов
        """
        return self.subscriber >= other.subscriber

    def __str__(self):
        return f"{self.title} {self.url}"
