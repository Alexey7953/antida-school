"""
31.2 Самый "пыльный" компакт-диск
Условие

Магазин компакт-дисков завален пыльными альбомами которые плохо продаются и хозяин хочет начать
распродажу старых альбомов. У Вас имеется xml-файл выгрузки из базы данных магазина компакт-дисков.
Хозяин называет Вам исполнителей, а вы должны проанализирвоать файл выгрузки и отсортировать альбомы
найденных исполнителей по двум параметрам: год и количество чтобы узнать самый старый и плохопродаваемый альбом.

Условие для входных данных: Строка-запрос, содержит:

Перечисленные через запятую (0 или более) имен исполнителей, имя может быть указано
частично, или целиком в любом регистре, например для строки: "Бон, бОб" будут
соответсовать исполнители "Бонни Тайлер" и "Боб Дилан".
Cтрока "all" - в этом случае поиск происходит по всем исполнителям.
Файл выгрузки находится рядом с файлом скрипта, ознакомиться с ним можно выполнив команду:

with open('catalog.xml') as file:
    print(file.read())

Формат вывода:

Если для указанных исполнителей не найдено ни одного альбома, то вывести сообщение: "Ничего не найдено"
Если альбомы найдены то вывести список альбомов в формате:
"Список найденных альбомов:"
<год> год. <количество> шт. "<заголовок альбома 1>" - <исполнитель 1>
...
<год> год. <количество> шт. "<заголовок альбома N>" - <исполнитель N>

Самый пыльный альбом: <год> год. <количество> шт. "<заголовок альбома N>" - <исполнитель N>
Самый свежий альбом: <год> год. <количество> шт. "<заголовок альбома N>" - <исполнитель N>
Сортировка альбомов происходит по двум параметрам: сначала по дате, потом по количеству компакт-дисков
Рекомендации к решению:

Изучите и используйте тип collections.namedtuple для описания простых сущностей.
Используйте функции для уменьшения дублирования кода.
Используйте стандартную библиотеку для париснга xml файла.
Требования:

Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
Не следует использовать классы.
"""

from collections import namedtuple
from xml.etree import ElementTree

Cd = namedtuple(
    'cd',
    ['artist', 'title', 'year', 'count']

)


def print_cd(item):
    print(f'{item.year} год. {item.count} шт. "{item.title}" - {item.artist}')


def create_cd(elem):
    return Cd(
        elem.get('artist'),
        elem.get('title'),
        int(elem.find('YEAR').text),
        int(elem.find('COUNT').text),
    )


incoming = input()
if incoming:
    incoming = [
        string.strip()
        for string in incoming.lower().split(',')  # ['name1', 'name2', ... 'nameN']
    ]
else:
    incoming = []

catalog = ElementTree.ElementTree(file='catalog.xml').getroot()
result = set()

if 'all' in incoming:

    for element in catalog.iter('CD'):

        result.add(create_cd(element))

else:

    for element in catalog.iter('CD'):
        for name in incoming:

            if element.get('artist').lower().count(name):

                result.add(create_cd(element))

if result:
    result = sorted(result, key=lambda x: (x.year, -x.count))
    print('Список найденных альбомов:')

    for cd in result:
        print_cd(cd)

    print()

    print('Самый пыльный альбом:', end=' ')
    print_cd(result[0])
    print('Самый свежий альбом:', end=' ')
    print_cd(result[-1])

else:
    print('Ничего не найдено')

# Коментарий от преподавателя

1. element.get('artist').lower().count(name) — лучше использовать name in element.get('artist').lower()

2. Хочется больше разбиения на функции, чтобы логика была сгруппирована. Например, отдельно парсинг XML в namedtuple,
отдельно фильтрация альбомов, отдельно вывод результата. Так код проще воспринимается

# Оптимальное решение

import xml.etree.ElementTree as ET
from collections import namedtuple

Album = namedtuple('Album', ['artist', 'title', 'year', 'count'])


def get_formated_album(album: Album) -> str:

    """ Возвращает строковое представление альбома """

    return f'{album.year} год. {album.count} шт. "{album.title}" - {album.artist}'


def artist_in_search(artist: str, search_keys: list) -> bool:

    """ Возвращает True/False, результат сопоставления поискового запроса и именем исполнителя

        Параметры:
            artist:       str, Имя исполнителя
            search_keys: list, Список фрагментов поискового запроса
            return:      bool, True если имя исполнителя содержит один из фрагментов поиска
    """

    result = False
    if artist:
        artist = artist.lower()
        for search_key in search_keys:
            if search_key.lower() in artist:
                result = True
    return result


def get_albumns(search_keys: list) -> list:

    """ Возвращает список альбомов из каталога согласно поисковому запросу

        Параметры:
            search_keys: list, список строк, каждая строка это часть имени исполнителя
            return:      list, список объектов типа Album,
                         отсортированных по году(по возрастанию) и количеству(по убыванию)

        Каталога хранится в виде xml файла со структурой:
            <CATALOG>
                <CD artist="Имя исполнителя" title="Название альбома">
                    <COUNTRY>Страна</COUNTRY>
                    <PRICE>Стоимость (целое число)</PRICE>
                    <YEAR>Год (четырехзначное число)</YEAR>
                    <COUNT>Количество (целое число)</COUNT>
                </CD>
                ...
                <CD>...</CD>
            </CATALOG>
    """

    search_all = 'all' in search_keys
    albums = set()
    xml_tree = ET.parse('catalog.xml')
    for tag in xml_tree.getroot():
        artist = tag.attrib['artist']
        if search_all or artist_in_search(artist=artist, search_keys=search_keys):
            albums.add(Album(
                artist=artist,
                title=tag.attrib['title'],
                year=int(tag.find('YEAR').text),
                count=int(tag.find('COUNT').text)
            ))
    sorted_albums = sorted(albums, key=lambda x: (x.year, -x.count))
    return sorted_albums


if '__main__' in __name__:
    search_keys = [key.strip() for key in input().split(',')]
    albums = get_albumns(search_keys=search_keys)
    if not albums:
        print("Ничего не найдено")
    else:
        dusty_album = albums[0]
        fresh_album = albums[-1]
        print('Список найденных альбомов:')
        for album in albums:
            print(get_formated_album(album=album))
        print(f'\nСамый пыльный альбом: {get_formated_album(album=dusty_album)}\n'
              f'Самый свежий альбом: {get_formated_album(album=fresh_album)}')
