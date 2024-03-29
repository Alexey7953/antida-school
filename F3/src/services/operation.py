import sqlite3

from database import db
from exceptions.operation import OperationNotFound


class OperationService:
    def __init__(self):
        self.connection = db.connection

    def create_operation(self, data: dict) -> int:
        """Создание операции в БД"""

        values = [value for value in data.values()]
        keys = [key for key in data.keys()]

        query = f"INSERT INTO operation (" + ','.join(keys) + ") VALUES (?, ?, ?, ?, ?, ?)"

        try:
            with self.connection as connection:
                cursor = connection.execute(query, values)
                connection.commit()
        except sqlite3.IntegrityError:
            raise OperationNotFound
        else:
            return cursor.lastrowid

