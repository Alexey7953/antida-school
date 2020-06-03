"""
Условие

Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет
делать запрос к БД и выводить результаты запроса в консоль.

Запрос:  Вывести список тегов, которые не выбраны ни для одного объявления.

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

with sqlite3.connect('example_2.db') as connection:
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT tag.name
        FROM tag
        WHERE NOT EXISTS(
            SELECT COUNT(ad.id) AS count
            FROM ad
                JOIN adtag ON tag.id = adtag.tag_id
            WHERE ad.id = adtag.ad_id
            GROUP BY ad.id
            HAVING count
        )
        """
    )

    for entry in cursor.fetchall():
        print(entry)
