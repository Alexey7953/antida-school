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
query = "INSERT INTO account (first_name, last_name, email, password) VALUES (?, ?, ?, ?);"
user_data = [
    ("Евгений", "Пирожков", "ex-1@mail.ru", "123465"),
    ("Макар", "Петрович", "ex-2@mail.ru", "123465"),
    ("Иванов", "Семенов", "ex-3@mail.ru", "123465"),
    ("Алена", "Петрова", "ex-4@mail.ru", "123465"),
]
cursor.executemany(query, user_data)
