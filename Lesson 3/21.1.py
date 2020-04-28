"""
Условие

Дан список элементов. Определите, сколько в нем встречается различных элементов.

Условие для входных данных: список чисел, разделенный пробелами, передается в консольный ввод одной строкой.

Условия для выходных данных: одно число - кол-во различных элементов

Требования:

Задание предназначено для закрепления навыков владения множествами.
Решите задачу в одну строку.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""

# Моё решение

print(len(set((map(str, input().split())))))

