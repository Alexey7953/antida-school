"""
Условие

Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет делать
запрос к БД и выводить результаты запроса в консоль.

Запрос: Вывести список автомобилей (таблица Car):

Для каждого автомобиля вывести поля "make", "model", "reg_number".
Заменить стандартные имена колонок на "Производитель", "Модель", "Регистрационный номер"
Требования:

Для запроса использовать только фразы SELECT и FROM.
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

    cursor.execute("""
    SELECT
        make        AS 'Производитель',
        model       AS 'Модель',
        reg_number  AS 'Регистрационный номер'
    FROM car;
    """)

    column_names = [description[0] for description in cursor.description]
    print(column_names)

    for record in cursor.fetchall():
        print(record)

