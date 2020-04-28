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
                )  # [(year1, str1), (year2, str2), ..., (yearN, strN)]

        except ValueError as e:
            pass

    if result:
        result.sort(key=lambda x: x[0])     # Сортируем по первым элементам кортежей (по year)

        print(f'За период {min_year}-{max_year} было выпущено: {len(result)} альбома(ов)')
        for year, text in result:
            print(f'{year}: {text}')

    else:
        print('Ничего не найдено')


if __name__ == '__main__':
    run()
