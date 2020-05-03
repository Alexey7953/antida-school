"""
35.1 Итоговое задание. Сортировщик файлов
Условие

Реализовать консольное (CLI) приложение для сортировки музыкальных файлов по исполнителям и альбомам:

Программа анализирует файлы в исходной директории, считывает ID3-теги, извлекает из них
информацию о названии трека, исполнителе и альбоме.
Группирует файлы (перемещает, не копирует) по исполнителям и альбомам, так, чтобы получить структуру директорий:
<директория назначения>/<исполнитель>/<альбом>/<имя файла>.mp3
Переименовывает файлы по схеме:
<название трека> - <исполнитель> - <альбом>.mp3
Если в тегах нет информации о названии трека, использует оригинальное имя файла.
Если в тегах нет информации об исполнителе или альбоме, пропускает файл, оставляя его без
изменений в исходной директории.
Если в целевой директории файл с таким названием уже существует - заменять его.
Программа должна принимать 3 ключа командной строки:
--help - вывести справочное сообщение;
-s | --src-dir - исходная директория, по умолчанию директория в которой запущен скрипт;
-d | --dst-dir - целевая директория, по умолчанию директория в которой запущен скрипт;.
В ходе работы программа должна выводить в консоль лог действий в виде:
<путь до исходного файла> -> <путь до файла результата>;
Программа должна корректно обрабатывать ошибки (не хватает прав доступа, директория не существует и т.д.)
и сообщать об этом пользователю, не прерывая свою работу (Текст сообщений на ваше успотрение).
Кроссплатформенная работа с файловой системой


Пример вызова справки приложения:

./sorter.py --help

Usage: sorter.py [OPTIONS]

Options:
    -s, --src-dir TEXT  Source directory.
    -d, --dst-dir TEXT  Destination directory.
    --help                     Show this message and exit.

Пример вызова приложения без параметров:

./sorter.py

...
./Du hast.mp3 -> ./Rammstein/Sehnsucht/Du hast - Rammstein - Sehnsucht.mp3
...
Done.

Пример вызова приложения с параметром целевой директории:

./sorter.py --dst-dir=/home/user/some/directory

...
./Du hast.mp3 -> /home/user/some/directory/Rammstein/Sehnsucht/Du hast - Rammstein - Sehnsucht.mp3
...
Done.

Рекомендации:

Для реализации консольного интерфейса рекомендуется использовать библиотеку Click или стандартный модуль argparse.
Для работы с ID3-тегами можно использовать библиотеки mp3-tagger или eyeD3, или любою другую на свое усмотрение.
Требования:

Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
Документирование модуля, функций, классов
Соблюдение PEP8 рекомендаций по стилевому оформлению кода
"""

import os
import argparse  # https://jenyay.net/Programming/Argparse
import eyed3

# Sorter
parser = argparse.ArgumentParser()
parser.add_argument(
    '-s',
    '--scr-dir',
    help='Source directory.',
    action='store',
    dest='src_dir',
    default=os.getcwd()
)
parser.add_argument(
    '-d',
    '--dst-dir',
    help='Destination directory.',
    action='store',
    dest='dst_dir',
    default=os.getcwd()
)

args = parser.parse_args()

# print(args.src_dir)
# print(args.dst_dir)

tree = os.walk(args.src_dir)  # https://pythoner.name/walk
for folder, _, files in tree:

    for file in files:
        if file.endswith('.mp3'):
            path = os.path.join(folder, file)
            print(os.path.join(folder, file))

            # Чтение тегов
            audiofile = eyed3.load(path)
            title = audiofile.tag.title
            artist = audiofile.tag.artist
            album = audiofile.tag.album

            if title:
                new_filename = f'{title} - {artist} - {album}.mp3'
            else:
                new_filename = file

            if artist and album:
                new_path = os.path.join(artist, album)
            else:
                continue

            new_file = os.path.join(args.dst_dir, new_path, new_filename)
            os.rename(path, new_file)


print('Done.')

