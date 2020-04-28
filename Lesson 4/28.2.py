"""
Условие

Напишите функцию поиска элемента последовательности, удовлетворяющего набору определенных условий.

Функция должна принимать следующие аргументы:

Любую итерируемую последовательность или коллекцию, в которой будет производиться поиск.
Сколько угодно функций-предикатов (функций, которые проверяют некоторое
условие для каждого элемента последовательности).
keyword-аргумент mode со значениями "and" или "or", определяющий, каким логическим оператором
объединять предикаты. По умолчания: "and".
keyword-аргумент default, определяющий значение, которое будет возвращено, если подходящий элемент не будет
найден в последовательности. По умолчанию: None.
Функция должна возвращать: первый элемент последовательности, который удовлетворяет
предикатам согласно mode, т.е. либо всем одновременно, либо любому из них.

Входные данные:

В 1 строке: последовательность действительных чисел, разделенных пробелами.
Во 2 строке: целое число N - количество предикатов.
В каждой из следующих N строк: текстовое представление предиката (пример: lambda x: x > 5)
В предпоследней строке: строки "and" или "or" - значение mode.
В последней строке: действительное число или строка "None" - значение default.
Выходные данные: результат поиска (действительное число или None).

Требования:

Основная программа должна содержать только код для чтения входных данных и вывода результата.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
Указания: для превращения строкового представления
предиката в функцию нужно воспользоваться функцией eval: https://docs.python.org/3/library/functions.html#eval
"""


def complicated_search(sequence, predicates, mode='and', default=None):
    sequence = list(map(float, sequence.split()))
    result = set()

    if mode.lower() == 'or':

        for predicate in predicates:
            result.update(
                filter(eval(predicate), sequence)
            )

    elif mode.lower() == 'and':
        result.update(sequence)

        for predicate in predicates:
            result.intersection_update(
                filter(eval(predicate), sequence)
            )

    for x in sequence:
        if x in result:
            return x


    try:
        return float(default)
    except ValueError:
        return None


    if default.lower() == 'none':
        return None
    return default

_sequence = input()
n = int(input())
_predicates = []
for _ in range(n):
    _predicates.append(input())
_mode = input()
_default = input()


print(complicated_search(sequence=_sequence, predicates=_predicates, mode=_mode, default=_default))
