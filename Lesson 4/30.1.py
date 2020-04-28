"""
Условие

Напишите декоратор count_calls, который подсчитывает, сколько раз была вызвана декорированная
им функция с определенным значением аргумента. Значение счетчика должно сохраняться в атрибут функции call_count.

Пример:

@count_calls(arg=3)
def func(x):
 pass

func(2)
func(3)
func(1)
func(3)
print(func.call_count) # 2
Входные данные:

В 1 строке: целое число - значение arg, какое значение должен учитывать декоратор.
Во 2 строке: список целых чисел через пробел, с каждым из которых нужно вызвать функцию.
Выходные данные: значение call_count.

Требования:

В качестве декорируемой можно использовать любую функцию, принимающую 1 аргумент.
Декоратор должен использовать wraps.
Основная программа должна содержать только код для чтения входных данных и вывода результата.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""

from functools import wraps


def count_calls(arg):
    def decorator(func):

        @wraps(func)
        def wrapper(func_arg):
            if func_arg == arg:
                wrapper.call_count += 1
            func(func_arg)

            return func

        wrapper.call_count = 0
        return wrapper
    return decorator


search_int = int(input())


@count_calls(search_int)
def f(i):
    pass


args_list = list(map(int, input().split()))

for argument in args_list:
    f(argument)

print(f.call_count)
