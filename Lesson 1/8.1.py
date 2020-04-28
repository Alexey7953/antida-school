"""
Напишите программу, которая читает из консоли одно натуральное число, суммирует
всех цифры числа и выводит значение в консоль.
Требования: Необходимо использовать цикл while
"""
# Моё решение

a = input()
b = 0
result = 0

while b < len(a):
    result += int(a[b])
    b += 1

print(result)

# Оптимальный вариант решения

number = int(input())
result_sum = 0
while(number > 0):
    result_sum += number % 10
    number //= 10
print(result_sum)