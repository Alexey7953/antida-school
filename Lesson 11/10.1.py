"""
Условие

В рамках проектирования базы данных мы создали физическую модель, а затем
на ее основе создали базу данных и набор отношений. Требования к БД были следующие:

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
Каждому автомобилю может соотв. 0 или более фотографий, фотографии
размещаются на любом хотинге в интернете, в базе хранятся только ссылки на фотографии.
Для каждой фотографии можно заполнить заголовок.
Требуется написать программу на языке Python 3 для СУБД Sqlite, которая будет
заполнять новые отношения данными согласно требованиям:

Создать не менее 5 новых записей в каждом отношении.
Если данные уже существуют в отношении - программа ничего об этом не знает и все равно записывает
данные еще раз, если возникает исключение - обработать его и вывести сообщение в консоль, не прерывая работы программы.
Предполагается что все отношения БД существуют, используйте файл БД из прошлой задачи (там создавали новые отношения).
Для написания программы ориентируйтесь на физическую модель.
Задача считается решенной, если после выполнения программы в БД добавятся новые данные или выведется
сообщение об ошибке если это невозможно.
"""
import sqlite3
from datetime import datetime

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()

    # Добавление данных в таблицу Account
    # Пример использования executemany()
    data = [
        ('Евгений', 'Разгуляев', 'box-1@mail.ru', 'secret-password'),
        ('Алекс', 'Миллер', 'box-2@mail.ru', 'secret-password'),
        ('Иванов', 'Семенов', 'box-3@mail.ru', 'secret-password'),
        ('Алена', 'Петрова', 'box-4@mail.ru', 'secret-password')
    ]
    query = """
        INSERT INTO account (first_name, last_name, email, password)
        VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, data)

    # Добавление данных в таблицу City
    # Пример использования execute()
    cursor.execute("""
        INSERT INTO city (name) 
        VALUES 
        ('Челябинск'),
        ('Москва'),
        ('Владивосток');
   """)

    # Добавление данных в таблицы ZipCode, Seller, Color, Car, CarColor
    # Пример использования executescript()
    cursor.executescript("""
        INSERT INTO zipcode (zip_code, city_id) 
        VALUES 
        ('454000', 1),
        ('101000', 2),
        ('690000', 3);

        INSERT INTO seller (zip_code, street, home, phone, account_id) 
        VALUES 
        ('454000', 'Раздольная', '5/A', '86541237845', 1),
        ('101000', 'Ленина', '125', '89198971212', 3);

        INSERT INTO color (name, hex) 
        VALUES 
        ('красный', 'ff0000'),
        ('синий', '000066'),
        ('зеленый', '339966'),
        ('желтый', 'FFFF00'),
        ('черный', '000000');

        INSERT INTO car (make, model, mileage, num_owners, reg_number)
        VALUES 
        ('Nissan', 'Patrol', '40500', 5, 'o423oo'),
        ('Mercedes', 'GLA', '5000', 1, 'x666xx'),
        ('ВАЗ', '2110', '10000', 2, 'м123ск'),
        ('УАЗ', 'Patriot', '25550', 3, 'п564оп'),
        ('Ford', 'GT', '100000', 4, 'к013ар'),
        ('Chevrolet', 'Impala 1965', '150000', 2, 'и555мп');

        INSERT INTO carcolor (color_id, car_id) 
        VALUES 
        ('1', '1'), 
        ('2', '1'), 
        ('3', '1'), 
        ('1', '2'), 
        ('2', '3'), 
        ('2', '4'),
        ('3', '4');    
    """)

    # Добавление данных в таблицу Ad
    # Пример использования форматированных строк
    date_1 = int(datetime(year=2019, month=12, day=1).timestamp())
    date_2 = int(datetime(year=2020, month=1, day=1, hour=12).timestamp())
    date_3 = int(datetime(year=2020, month=1, day=15).timestamp())
    date_4 = int(datetime(year=2018, month=2, day=27).timestamp())
    date_5 = int(datetime(year=2020, month=3, day=13).timestamp())

    cursor.execute(f"""
        INSERT INTO ad (title, date, car_id, seller_id) 
        VALUES 
        ('Продам внедорожник', {date_1}, 1, 1),
        ('Продам внедорожник с пробегом', {date_2}, 1, 1),
        ('Продам мерседес после восстановления', {date_3}, 2, 2),
        ('Десятка в хорошем состоянии', {date_4}, 3, 2),
        ('Уаз в люкс комплектации', {date_5}, 4, 2);
    """)