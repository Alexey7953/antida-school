"""
Условие

Для указанного натурального числа подсчитайте количество установленных (= 1) битов в его двоичной записи.

Условие для входных данных: натуральное число N.

Условие вывода: одно число - количество установленных битов в числе N.

Требования:

Задание предназначено для закрепления навыков владения побитовыми операциями с числами.
Запрещается использование математических операций, кроме побитовых с числом N.
Запрещается использование опраций со строками, кроме ввода.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""
# Моё решение

number = bin(int(input()))
num_list = []
for num in number:
    if num == '1':
        num_list.append(num)
print(len(num_list))
