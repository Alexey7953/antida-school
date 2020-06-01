import sqlite3

from blueprints import colors
from src.exceptions import ServiceError


class ColorServiceError(ServiceError):
    service = 'color'


class ColorService:
    def __init__(self, connection):
        self.connection = connection

    def read_all_color(self):
        """ Получение списка всех цветов """
        query = (
            """
            SELECT *
            FROM color
            """
        )
        cursor = self.connection.execute(query)
        return [dict(entry) for entry in cursor.fetchall()]

    def read_color(self, color_id):
        query = (
            """
            SELECT *
            FROM color
            WHERE id = ?
            """
        )
        params = (color_id, )
        cursor = self.connection.execute(query, params)
        color = cursor.fetchone()

        if color is None:
            raise ColorServiceError
        return dict(color)

    def create_color(self, name, hex_id):
        """ Создание цвета """
        query = (
            """
            INSERT INTO color (name, hex) VALUES (?, ? )
            """
        )
        params = (name, hex_id)

        try:
            cursor = self.connection.execute(query, params)
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise ColorServiceError

        return cursor.lastrowid
