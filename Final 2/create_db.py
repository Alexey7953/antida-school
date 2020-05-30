import os
import sqlite3


def create_db(db):
    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()

        # 1 Создание отношения Account
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS account ("
            "id 		INTEGER PRIMARY KEY AUTOINCREMENT,"
            "first_name TEXT    NOT NULL,"
            "last_name 	TEXT    NOT NULL,"
            "email 		TEXT    NOT NULL UNIQUE,"
            "password 	TEXT    NOT NULL"
            ");"
        )

        # 2 Создание отношения City
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS city ("
            "id 	INTEGER PRIMARY KEY AUTOINCREMENT,"
            "name   TEXT NOT NULL"
            ");"
        )

        # 3 Создание отношения ZipCode
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS zipcode ("
            "zip_code	 INTEGER PRIMARY KEY,"
            "city_id     INTEGER NOT NULL REFERENCES city(id)"
            ");"
        )

        # 4 Создание отношения Seller
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS seller ("
            "id 		 INTEGER PRIMARY KEY AUTOINCREMENT,"
            "zip_code    INTEGER NOT NULL REFERENCES zipcode(zip_code),"
            "street      TEXT NOT NULL,"
            "home        TEXT NOT NULL,"
            "phone       TEXT NOT NULL,"
            "account_id  INTEGER NOT NULL REFERENCES account(id)"
            ");"
        )

        # 5 Создание отношения Color
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS color ("
            "id     INTEGER PRIMARY KEY AUTOINCREMENT,"
            "name   TEXT NOT NULL,"
            "hex    TEXT NOT NULL"
            ");"
        )

        # 6 Создание отношения Car
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS car ("
            "id                 INTEGER PRIMARY KEY AUTOINCREMENT,"
            "make               TEXT NOT NULL,"
            "model              TEXT NOT NULL,"
            "mileage            INTEGER  NOT NULL,"
            "num_owners         INTEGER NOT NULL,"
            "reg_number         TEXT NOT NULL"
            ")"
        )
        # 7 Создание отношения CarColor
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS carcolor ("
            "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
            "color_id   INTEGER NOT NULL REFERENCES color(id),"
            "car_id     INTEGER NOT NULL REFERENCES car(id)"
            ");"
        )

        # 8 Создание отношения Ad
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS ad ("
            "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
            "title      TEXT NOT NULL,"
            "date       INTEGER NOT NULL,"
            "seller_id  INTEGER NOT NULL REFERENCES seller(id),"
            "car_id     INTEGER NOT NULL REFERENCES car(id)"
            ")"
        )

        # 9 Создание отношения Tag
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tag (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    name       TEXT NOT NULL UNIQUE
                    );            
                """)

        # 10 Создание отношения AdTag
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS adtag (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    tag_id      INTEGER NOT NULL REFERENCES tag(id),
                    ad_id       INTEGER NOT NULL REFERENCES ad(id)
                    );
                """)

        # 11 Создание отношения Image
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS image (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    title       TEXT,
                    url         TEXT NOT NULL,
                    car_id      INTEGER
                    );
                """)


if __name__ == '__main__':
    answer = input('Создать пустую базу данных? (y/n): ')

    if answer.lower() == 'y':

        db_path = os.getenv('DB_CONNECTION', 'db.sqlite')

        if os.path.exists(db_path):
            os.remove(db_path)
            print('Старая база удалена.')

        create_db(db=db_path)
        print(f'Создана база: "{db_path}"')
