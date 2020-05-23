"""
Условие

Реализовать REST API сервиса по продаже автомобилей.
За основу взять предметную область, описанную в курсе "Базы данных".

Описание API:
Авторизация: вход и выход.

POST /auth/login
Request:
{
  "email": str,
  "password": str
}

POST /auth/logout
Регистрация пользователя. Поле is_seller показывает, является ли пользователь продавцом.
Поля phone, zip_code, city_id, street, home указываются, только если пользователь является продавцом.

POST /users
Request:
{
  "email": str,
  "password": str,
  "first_name": str,
  "last_name": str,
  "is_seller": bool,
  "phone": str?,
  "zip_code": int?,
  "city_id": int?,
  "street": str?,
  "home": str?
}
Response:
{
  "id": int,
  "email": str,
  "first_name": str,
  "last_name": str,
  "is_seller": bool,
  "phone": str?,
  "zip_code": int?,
  "city_id": int?,
  "street": str?,
  "home": str?
}
Получение пользователя. Доступно только авторизованным пользователям.

GET /users/<id>
Response:
{
  "id": int,
  "email": str,
  "first_name": str,
  "last_name": str,
  "is_seller": bool,
  "phone": str?,
  "zip_code": int?,
  "city_id": int?,
  "street": str?,
  "home": str?
}
Частичное редактирование пользователя. Доступно только текущему авторизованному пользователю.
Поля phone, zip_code, city_id, street, home указываются, только если пользователь является продавцом.
При установке флага is_seller в false должно происходить удаление сущностей продавца.

PATCH /users/<id>
Request:
{
  "first_name": str?,
  "last_name": str?,
  "is_seller": bool?,
  "phone": str?,
  "zip_code": int?,
  "city_id": int?,
  "street": str?,
  "home": str?
}
Response:
{
  "id": int,
  "email": str,
  "first_name": str,
  "last_name": str,
  "is_seller": bool,
  "phone": str?,
  "zip_code": int?,
  "city_id": int?,
  "street": str?,
  "home": str?
}
Получение списка объявлений: всех и принадлежащих пользователю.
Список можно фильтровать с помощью query string параметров, все параметры необязательные.

GET /ads
GET /users/<id>/ads
Query string:
  seller_id: int?
  tags: str?
  make: str?
  model: str?
Response:
[
  {
    "id": int,
    "seller_id": int,
    "title": str,
    "posted": str,
    "tags:": [str], // Список тегов строками
    "car": {
      "make": str,
      "model": str,
      "colors": [
        {
          "id": int,
          "name": str,
          "hex": str
        }
      ],
      "mileage": int,
      "num_owners": int,
      "reg_number": str,
      "images": [
        {
          "title": str,
          "url": str
        }
      ]
    }
  }
]
Публикация объявления. Доступно только авторизованным пользователям.
Доступно только если пользователь является продавцом.

POST /ads
POST /users/<id>/ads
Request:
{
  "title": str,
  "tags": [str, ...], // Список тегов строками
  "car": {
    "make": str,
    "model": str,
    "colors": [int], // Список ID цветов
    "mileage": int,
    "num_owners": int?,
    "reg_number": str,
    "images": [
      {
        "title": str,
        "url": str
      }
    ]
  }
}
Response:
{
  "id": int,
  "seller_id": int,
  "title": str,
  "posted": str,
  "tags:": [str], // Список тегов строками
  "car": {
    "make": str,
    "model": str,
    "colors": [
      {
        "id": int,
        "name": str,
        "hex": str
      }
    ],
    "mileage": int,
    "num_owners": int,
    "reg_number": str,
    "images": [
      {
        "title": str,
        "url": str
      }
    ]
  }
}
Получение объявления.

GET /ads/<id>
Response:
{
  "id": int,
  "seller_id": int,
  "title": str,
  "posted": str,
  "tags:": [str], // Список тегов строками
  "car": {
    "make": str,
    "model": str,
    "colors": [
      {
        "id": int,
        "name": str,
        "hex": str
      }
    ],
    "mileage": int,
    "num_owners": int,
    "reg_number": str,
    "images": [
      {
        "title": str,
        "url": str
      }
    ]
  }
}
Частичное редактирование объявления. Доступно только авторизованным пользователям.
Может совершать только владелец объявления.

PATCH /ads/<id>
Request:
{
  "title": str?,
  "tags": [str]?, // Список тегов строками
  "car": {
    "make": str?,
    "model": str?,
    "colors": [int]?, // Список ID цветов
    "mileage": int?,
    "num_owners": int?,
    "reg_number": str?,
    "images": [
      {
        "title": str,
        "url": str
      }
    ]?
  }
}
Удаление объявления. Доступно только авторизованным пользователям. Может совершать только владелец объявления.

DELETE /ads/<id>
Получение списка городов.

GET /cities
Response:
[
  {
    "id": int,
    "name": str
  }
]
Создание города. При попытке создать уже существующий город (проверка по названию), должен
возвращаться существующий объект.

POST /cities
Request:
{
  "name": str
}
Response:
{
  "id": int,
  "name": str
}
Получение списка цветов. Доступно только авторизованным пользователям.
Доступно только если пользователь является продавцом.

GET /colors
Response:
[
  {
    "id": int,
    "name": str,
    "hex": str
  }
]
Создание цвета. Доступно только авторизованным пользователям. Доступно только если пользователь является продавцом.
При попытке создать уже существующий цвет (проверка по названию), должен возвращаться существующий объект.

POST /colors
Request:
{
  "name": str,
  "hex": str
}
Response:
{
  "id": int,
  "name": str,
  "hex": str
}
Загрузка изображения. Доступно только авторизованным пользователям. Доступно только если пользователь является продавцом.

POST /images
Request:
  файл изображения в поле формы
Response:
{
  "url": str
}
Получение изображения.

GET /images/<name>
Response:
  файл изображения


Требования:

Приложение должно быть реализовано с помощью web-фреймворка Flask.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
Документирование модулей, функций, классов.
Соблюдение PEP8 рекомендаций по стилевому оформлению кода.
Исходный код решения должен быть загружен в систему контроля версий и опубликован на github,
в качестве решения нужно приложить ссылку на репозиторий.
В репозитории должен присутствовать файл requirements.txt со списком зависимостей и файл README.md
с инструкцией по запуску приложения.
Примечания
Формат описания запросов/ответов:

запросы и ответы представлены в JSON-подобной структуре и описывают JSON-документы
через двоеточие указываются типы полей
запись вида type? обозначает, что поле необязательное и может отсутствовать
запись вида [type] обозначает список значений типа type
При тестировании приложения гарантируется корректность входных данных.

Примеры тестовых сценариев работы с API:

Регистрация пользователя и авторизация:

POST /users
{
  "email": "johndoe@example.com",
  "password": "password",
  "first_name": "John",
  "last_name": "Doe",
  "is_seller": false
}

POST /auth/login
{
  "email": "johndoe@example.com",
  "password": "password"
}

GET /users/<id нового пользователя>


Регистрация продавца, авторизация, создание объявления и необходимых сущностей.

POST /cities
{
  "name": "Москва"
}

POST /users
{
  "email": "janedoe@example.com",
  "password": "password",
  "first_name": "Jane",
  "last_name": "Doe",
  "is_seller": true,
  "phone": "+75551112233",
  "zip_code": "555123",
  "city_id": <id города>,
  "street": "Пушкина",
  "home": 42
}

POST /auth/login
{
  "email": "janedoe@example.com",
  "password": "password"
}

POST /colors
{
  "name": "red",
  "hex": "ff1122"
}

POST /images
фото1

POST /images
фото2

POST /ads
{
  "title": "Продам жигуль",
  "tags": ["жигуль", "ваз", "таз", "машинамечты"],
  "car": {
    "make": "ВАЗ",
    "model": "2101",
    "colors": [<id цвета>],
    "mileage": 200000,
    "num_owners": 7,
    "reg_number": "В666АЗ",
    "images": [
      {"title": "Перед", "url": "<url фото1>"},
      {"title": "Зад", "url": "<url фото2>"}
    ]
  }
}

GET /users/<id пользователя>/ads/<id объявления>
"""