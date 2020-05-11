import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS account ("
    "id 		INTEGER PRIMARY KEY AUTOINCREMENT,"
    "first_name TEXT    NOT NULL,"
    "last_name 	TEXT    NOT NULL,"
    "email 		TEXT    NOT NULL UNIQUE,"
    "password 	TEXT    NOT NULL"
    ");"
)
