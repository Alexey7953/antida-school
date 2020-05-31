import sqlite3
from blueprints import image
from src.exceptions import ServiceError


class ImageServiceError(object):
    pass


class ImageService:
    def __init__(self, connection):
        self.connection = connection

    def create_image(self, url):
        # Запись изображения в базу данных
        query = (
            """
            INSERT INTO image (url, car_id) VALUES (?, 0)
            """
        )
        params = (url,)
        try:
            self.connection.execute(query, params)
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise ImageServiceError
