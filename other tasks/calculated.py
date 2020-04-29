def calculate(a, b, c):
    d = b ** 2 - (4 * a * c)

    if a == 0:
        if b != 0:
            x = -c / b
            print(f'x = {x}')
        else:
            print('x может принимать любое значение')

    elif d == 0:
        x = -b / (2 * a)
        print(f'x = {x}')

    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f'x1 = {x1}\nx2 = {x2}')

    else:
        print('Нет действительных корней')

    return


if __name__ == '__main__':
    while True:
        try:
            print('Оставте все значения пустыми для завершения работы')
            print('Уравнение: A*x*x + B*x + C = 0')

            print('Введите A:')
            a = float(input())
            print('Введите B:')
            b = float(input())
            print('Введите C:')
            c = float(input())

            if not all([a, b, c]):
                break

            calculate(a, b, c)

        except ValueError:
            print('Введите число!')

        except Exception as e:
            print(f'Ошибка: {e}')

    print('Завершение работы.')
