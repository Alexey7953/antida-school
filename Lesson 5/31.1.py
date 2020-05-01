"""
Условие

Вы истинный ценитель музыки и у Вас есть данные по всем музыкальным альбомам выпущеным за последние 30 лет.
Вы по спорили с другом на новую гитару что назовете точное число альбомов выпущенных за некоторый промежуток времени,
чтобы быть уверенным в правоте требуется написать программу, которая анализирует данные.

Условие для входных данных: Две строки, дата начала и дата конца периода, например 1995 и 2000

Данные по музыкальным альбомам хранятся в xml-файле.
Файл находится рядом с файлом скрипта, ознакомиться с ним можно выполнив команду:

with open('catalog.xml') as file:
    print(file.read())

Формат вывода:

Если за указанный период не было выпущено ни одного альбома, вывести сообщение: "Ничего не найдено"
Если за указанный период были выпущены альбомы, то вывести сообщение и список альбомов в формате:
За период <дата начала>-<дата окончания> было выпущено: <количество> альбома(ов)
<год 1>: <исполнитель 1> - "<название альбома 1>"
...
<год N>: <исполнитель N> - "<название альбома N>"
Список альбомов должен быть отсорирован по возрастанию даты.

Рекомендации к решению:

Используйте стандартную библиотеку для париснга xml файла.
Требования:

Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
Не следует использовать классы.
"""

from xml.etree import ElementTree


def run():
    try:
        min_year = int(input())
        max_year = int(input())
    except ValueError:
        print('Years set wrong. quit program...')
        return

    result = []
    catalog = ElementTree.ElementTree(file='catalog.xml').getroot()

    for cd in catalog.iter('CD'):
        try:
            year = int(cd.find('YEAR').text)

            if min_year <= year <= max_year:
                result.append(
                    (year, f'{cd.get("artist")} - "{cd.get("title")}"')
                )

        except ValueError as e:
            pass

    if result:
        result.sort(key=lambda x: x[0])

        print(f'За период {min_year}-{max_year} было выпущено: {len(result)} альбома(ов)')
        for year, text in result:
            print(f'{year}: {text}')

    else:
        print('Ничего не найдено')


if __name__ == '__main__':
    run()

# Решение от преподавателя

import xml.etree.ElementTree as ET

tree = ET.parse('catalog.xml')
albums = []
date_start, date_end = int(input()), int(input())

for tag in tree.getroot():
    year = int(tag.find('YEAR').text)
    if year >= date_start and year <= date_end:
        artist = tag.attrib['artist']
        title = tag.attrib['title']
        albums.append((year, f'{artist} - "{title}"'))

if not albums:
    print('Ничего не найдено')
else:
    albums.sort(key=lambda x: x[0])
    print(f'За период {date_start}-{date_end} было выпущено: {len(albums)} альбома(ов)')
    for album in albums:
        year, title = album
        print(f'{year}: {title}')
