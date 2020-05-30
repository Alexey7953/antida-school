"""
Условие

Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет делать
запрос к БД и выводить результаты запроса в консоль.

Запрос:  Вывести список продавцов, для каждого продавца вывести имя и фамилию и количество
созданных им объявлений. Отсортировать результат по кол-ву созданных объявлений по убыванию.

Требования:

Python допустимо использовать только для подключения к БД, выполнения запроса и вывода данных.
Обработка данных должна производиться только языком SQL.
Следуйте Python Zen и PEP8, код должен быть минималистичным, лаконичным, но хорошо читаемым.
Следуйте рекомендациям SQL Style Guide при написании запросов.
Рекомендации:

Задача проверяется на файле БД, который вы можете скачать по ссылке.
При выполнении программы на сайте - файл БД располагается рядом со скриптом и его можно открыть вот так:
with sqlite3.connect('example_2.db') as connection:
    cursor = connection.cursor()
"""
import sqlite3
with sqlite3.connect('example.db') as connection:

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT account.first_name, account.last_name, COUNT(ad.id) as count
        FROM account
            JOIN seller ON account.id = seller.account_id
            JOIN ad ON seller.id = ad.seller_id
        GROUP BY account.id
        ORDER BY count DESC
        """
    )

    for entry in cursor.fetchall():
        print(entry)
