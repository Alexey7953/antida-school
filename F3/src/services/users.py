import sqlite3

from src.exceptions import ServiceError


class UsersServiceError(ServiceError):
    service = 'users'


def read_user(user_id):
    query = (
        """
    SELECT id, first_name, last_name, email
    FROM account
    WHERE id = ?
        """
        )
