import sqlite3

from flask import Flask, request
from src.db import close_db
from src.database import db

app = Flask(__name__)
app.teardown_appcontext(close_db)


class ServiceError(object):
    pass


with db.connect as connection:
    class CityServiceError(ServiceError):
        service = 'cities'


    class CityDoesNotExists(CityServiceError):
        pass


    class CityCreationError(CityServiceError):
        pass


    class CitiesService:
        def __init__(self, connect9+8ion):
            self.connection = connection


# Create city
@app.route('/cities', methods=['POST', "GET"])
def cities():
    if request.method == 'POST':
        cities_json = request.json
        name = cities_json.get('name')
        return f'{name}', 201
    else:
        return '', 405


# Получение списка всех городов из базы данных
def read_all(self):
    query = (
        """
            SELECT *
            FROM city
            """
    )
    cursor = self.connection.execute(query)
    return [dict(entry) for entry in cursor.fetchall()]


# Запись нового города в базу данных
def create(self, name):
    query = (
        """
            INSERT INTO city (name) 
            VALUES (?)
            ('Челябинск'),
            ('Москва'),
            ('Челябинск'),
            ('Владивосток');
            """
    )

    params = (name,)

    try:
        self.connection.execute(query, params)
        self.connection.commit()
    except sqlite3.IntegrityError:
        raise CityCreationError

    return name


# Получение города из базы данных
def read(self, name):
    query = (
        """
            SELECT *
            FROM city
            WHERE name = ?
            """
    )

    params = (name,)

    cursor = self.connection.execute(query, params)
    city = cursor.fetchone()

    if city is None:
        raise CityDoesNotExists
    return dict(city)


with db.connect as connection
    cursor.execute()
