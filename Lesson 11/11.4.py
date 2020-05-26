"""
Условие

Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет
делать запрос к БД и выводить результаты запроса в консоль.

Запрос: Вывести список автомобилей у которых было от одного до трех владельцев:

Для каждого автомобиля вывести поля "num_owners", "make", "model".
Отсортировать выборку по убыванию количества владельцев.
Не выводить названия колонок таблицы.
Требования:

Для запроса использовать только фразы SELECT, FROM, WHERE, ORDER BY.
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
        "SELECT num_owners, make, model "
        "FROM car "
        "WHERE num_owners BETWEEN 1 AND 3 "
        "ORDER BY num_owners DESC "

    )
    for record in cursor.fetchall():
        print(record)
