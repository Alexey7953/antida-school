"""
33.1 Рога и Копыта
Условие

В компании "Рога и Копыта" работают менеджеры, техники и водители:

Менеджеры и техники получают фиксированную ежемесячную зарплату.
У водителей оплата почасовая.
Заработная плата техников и водителей зависит от их категории (A, B или C).
Категория предоставляет коэффициент от базовой зарплаты: A - 125%, B - 115%, С - 100%.
Все работники могут получить фиксированную ежемесячную премию, которая прибавляется к их основной заработной плате.
Напишите программу, которая получает информацию о работниках
компании и вычисляет, сколько компания должна выплатить своим сотрудникам в конце месяца.

Входные данные:

В первой строке: целое число N - количество сотрудников в компании.
В каждой из следующих N строк - информация о сотрудниках в виде набора полей через пробел:
профессия (manager, technician или driver)
вещественное число - базовая заработная плата (для сотрудников с почасовой оплатой - стоимость часа)
вещественное число - размер премии сотрудника
целое число - количество отработанных часов (для сотрудников с фиксированной оплатой - 0)
строка "A", "B" или "C" - категория сотрудника, присутствует только у техника и водителя
Выходные данные: вещественное число - суммарный размер выплат по заработной плате всех сотрудников.

Требования:

Программу необходимо реализовать в виде иерархии классов с минимальным объемом дублирования.
Иерархия должна поддерживать возможность расширения. К примеру, могут появиться
сотрудники с почасовой зарплатой, не привязанной к категориям или с доплатой за переработку при привышении нормы часов.
Реализовывать данное поведение не нужно, но оно должно быть легко внедряемым.
Следуйте Python Zen: код должен быть минималистичным, лаконичным, но хорошо читаемым.
"""


class Employee(object):

    def __init__(self, base_payment, prize, hours):
        self.base_payment = float(base_payment)
        self.hours = int(hours)
        self.prize = float(prize)

    def _payment(self):
        return self.base_payment

    def count_salary(self):
        return self._payment() + self.prize


class EmployeeCategory(Employee):
    """коэффициент базовой зарплаты"""

    categories = {
        'a': 1.25,
        'b': 1.15,
        'c': 1.0
    }

    def __init__(self, base_payment, prize, hours, category):
        super().__init__(base_payment, prize, hours)
        self.category = self.categories[category]

    def _payment(self):
        return super()._payment() * self.category


class EmployeeHours(Employee):
    """Класс сотрудников организации с почасовой ставкой"""

    def _payment(self):
        return super()._payment() * self.hours


class Manager(Employee):
    """Класс менеджер"""
    pass


class Technician(EmployeeCategory):
    """Класс техника"""
    pass


class Driver(EmployeeHours, EmployeeCategory):
    """Класс водителя"""
    pass


if __name__ == '__main__':

    total_salary = 0
    employers = int(input())

    for i in range(employers):
        employee_info = input().lower().split()
        position = employee_info.pop(0)

        if position == 'manager':
            base_payment, prize, hours = employee_info
            total_salary += Manager(base_payment, prize, hours).count_salary()

        elif position == 'technician':
            base_payment, prize, hours, category = employee_info
            total_salary += Technician(base_payment, prize, hours, category).count_salary()

        elif position == 'driver':
            base_payment, prize, hours, category = employee_info
            total_salary += Driver(base_payment, prize, hours, category).count_salary()

    print(total_salary)
