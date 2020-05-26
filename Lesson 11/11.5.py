"""
Условие

Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет 
делать запрос к БД и выводить результаты запроса в консоль.

Запрос: Вывести все объявления у которых в заголовке содержится слово "внедорожник":

Для каждого объявления вывести поля "title", "car.make", "car.model".
Не выводить названия колонок таблицы.
Требования:

Для запроса использовать только фразы SELECT, FROM, WHERE.
Python допустимо использовать только для подключения к БД, выполнения запроса и вывода данных.
Обработка данных должна производиться только языком SQL.
Следуйте Python Zen и PEP8, код должен быть минималистичным, лаконичным, но хорошо читаемым.
Следуйте SQL Style Guide при написании запросов.
Рекомендации:

Задача проверяется на файле БД, который вы можете скачать по ссылке.
При выполнении программы на сайте - файл БД располагается рядом со скриптом и его можно открыть вот так:
with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()
"""
import sqlite3
with sqlite3.connect('example.db') as connection:

    cursor = connection.cursor()

    cursor.execute(
        "SELECT title, car.make, car.model "
        "FROM car "
        "JOIN ad ON car.id=ad.car_id "
        "WHERE title LIKE '%внедорожник%'"
    )
    for elem in cursor.fetchall():
        print(elem)
