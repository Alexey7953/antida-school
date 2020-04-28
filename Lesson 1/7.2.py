"""
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
сначала для первой клетки, потом для второй клетки.

Условие для входных данных: четыре целых числа (от одного до восьми включительно), каждое с новой строки:

номер столбца первой клетки
номер строки первой клетки
номер столбца второй клетки
номер строки второй клетки
Формат вывода: текстовое сообщение: YES или NO

Требования:

Задание предназначено для закрепления навыков владения условной инструкцией if.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""
# Моё решение

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

# Оптимальное решение

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
