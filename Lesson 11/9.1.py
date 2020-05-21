"""
Условие

    В рамках проектирования базы данных мы создали физическую модель, а затем на ее основе создали
    базу данных и набор отношений. Требования к БД были следующие:

    Предметная область: "Сайт для торговли автомобилями".
    Словесное описание требований:

Сайт представляет из себя площадку для размещения объявлений о продаже автомобилей.
Для работы на сайте необходима регистрация, обязательные поля профиля - Имя, Фамилия, Email, пароль.
Для авторизации используется пара Email и пароль.
Зарегистрированный пользователь может искать и просматривать объявления.
Зарегистрированный пользователь может размещать объявления только после того как
укажет в профилеа адрес по прописке и номер телефона.
При создании объявления указываются обязательные поля:
Дата создания (выставляется автоматически в момент создания объявления).
Заголовок.
Автомобиль.
Автомобиль должен содержать следующую информацию:
Марка.
Модель.
Регистрационный номер.
Владельцев по ПТС.
Пробег.
Цвет (можно указать несколько цветов).
Каждое объявление содержит только один автомобиль, но каждый автомобиль может участвовать в нескольких объявлениях.
Задание: На второй итерации разработки пришел следующий список требований от заказчика:

Каждому обьявлению может соответствовать 0 или более тегов, например:
"семейный, заниженный, спортивный, люкс и т.п." Каждый тег содержит уникальное название.
Каждому автомобилю может соотв. 0 или более фотографий, фотографии размещаются на любом
хотинге в интернете, в базе хранятся только ссылки на фотографии.
Для каждой фотографии можно заполнить заголовок.
Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет
создавать новые отношения согласно требованиям:

Если отношение уже существует программа не должна вызвать исключения, а успешно
завершиться, так же как и в случае если отношения будут созданы.
Предполагается что отношения созданные на прошлом этапе уже существуют, для проверки программы
использовать этот файл базы данных: скачать.
Для написания программы ориентируйтесь на физическую модель.
Задача считается решенной, если после выполнения программы в базе создатутся
новые отношения и они будут соотв. физической модели.
"""
import sqlite3

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()

    # 1 Создание таблицы Account
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS account ("
        "id 		INTEGER PRIMARY KEY AUTOINCREMENT,"
        "first_name TEXT    NOT NULL,"
        "last_name 	TEXT    NOT NULL,"
        "email 		TEXT    NOT NULL UNIQUE,"
        "password 	TEXT    NOT NULL"
        ");"
    )
    # 2 Создание таблицы City
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS city ("
        "id 	INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name   TEXT NOT NULL"
        ");"
    )
    # 3 Создание таблицы ZipCode
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS zipcode ("
        "zip_code	 INTEGER PRIMARY KEY,"
        "city_id     INTEGER NOT NULL REFERENCES city(id)"
        ");"
    )
    # 4 Создание таблицы Seller
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
    # 5 Создание таблицы Color
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS color ("
        "id     INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name   TEXT NOT NULL,"
        "hex    TEXT NOT NULL"
        ");"
    )
    # 6 Создание таблицы Car
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS car ("
        "id                 INTEGER PRIMARY KEY AUTOINCREMENT,"
        "make               TEXT NOT NULL,"
        "model              TEXT NOT NULL,"
        "mileage            INTEGER  NOT NULL,"
        "num_owners         INTEGER NOT NULL DEFAULT 1,"
        "reg_number         TEXT NOT NULL"
        ")"
    )
    # 7 Создание таблицы CarColor
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS car_color("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "color_id   INTEGER NOT NULL REFERENCES color(id),"
        "car_id     INTEGER NOT NULL REFERENCES car(id)"
        ");"
    )
    # 8 Создание таблицы Ad
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ad ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "title      TEXT NOT NULL,"
        "date       INTEGER NOT NULL,"
        "seller_id  INTEGER NOT NULL REFERENCES seller(id),"
        "car_id     INTEGER NOT NULL REFERENCES car(id)"
        ")"
    )
    # 9 Создание таблицы Image
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS image ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "title      TEXT,"
        "url        TEXT NOT NULL,"
        "car_id     INTEGER NOT NULL REFERENCES car(id)"
        ")"
    )
    # 10 Создание таблицы Tag
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tag ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name       TEXT NOT NULL UNIQUE"
        ")"
    )
    # 11 Создание таблицы AdTag
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ad_tag ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "tag_id     INTEGER NOT NULL REFERENCES tag(id),"
        "ad_id      INTEGER NOT NULL REFERENCES ad(id)"
        ")"
    )



