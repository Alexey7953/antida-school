"""
Условие

Даны два целых числа A и В. Выведите все нечётные числа от A до B включительно, в порядке убывания.

Условие для входных данных: два целых числа  A и В, что A > B, каждое с новой строки.

Формат вывода: список чисел через пробел в одну строку

Требования:

Задание предназначено для закрепления навыков владения инструкцией for.
Не следует использовать условную инструкцию if.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""
# Моё решение

a = int(input())
b = int(input())

result = []

for x in range(b, a + 1):
    x % 2 and result.append(x)



print(*reversed(result))

# Оптимальное решение

a=int(input())
b=int(input())
# коэф. вычисляем на основе четности a
coef = int(a%2==0) # int(True) = 1, int(False) = 0
start = a - coef
end = b-1
step = -2
for i in range(start, end, step):
    print(i, end=' ')