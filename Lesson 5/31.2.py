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
"""
1. element.get('artist').lower().count(name) — лучше использовать name in element.get('artist').lower()

2. Хочется больше разбиения на функции, чтобы логика была сгруппирована. Например, отдельно парсинг XML в namedtuple,
отдельно фильтрация альбомов, отдельно вывод результата. Так код проще воспринимается
"""