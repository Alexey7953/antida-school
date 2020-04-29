print('Введите коэффициенты для квадратного уравнения ax^2 + bx + c = 0')
a = float(input("Введите значение a = "))
b = float(input("Введите значение b = "))
c = float(input("Введите значение c = "))
d = b**2-4*a*c
if a == 0:
    if b != 0:
        x = -c / b
        print(f'x = {x}')
    else:
        print('x может принимать любое значение')
elif d > 0:
    x1 = (-b+d**0.5) / (2*a)
    x2 = (-b-d**0.5) / (2*a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
elif d == 0:
    print(f'x = {-b/(2*a)}')
else:
    print('Нет действительных корней')
