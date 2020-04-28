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
        self.prize = float(prize)
        self.hours = int(hours)

    def _payment(self) -> float:
        return self.base_payment

    def count_salary(self) -> float:
        return self._payment() + self.prize


class Category_with_workers(Employee):
    categories = {
        'a': 1.25,
        'b': 1.15,
        'c': 1.0
    }

    def __init__(self, base_payment, prize, hours, category):
        super().__init__(base_payment, prize, hours)
        self.category = self.categories[category]

    def _payment(self) -> float:
        return super()._payment() * self.category


class WorkerRateByHours(Employee):
    def _payment(self):
        return super()._payment() * self.hours


class Manager(Employee):
    pass


class Technician(Category_with_workers):
    pass


class Driver(WorkerRateByHours, Category_with_workers):
    pass


if __name__ == '__main__':

    total_salary = 0
    number_of_workers = int(input())

    for i in range(number_of_workers):
        worker_info = input().lower().split()
        position = worker_info.pop(0)

        if position == 'manager':
            total_salary += Manager(*worker_info).count_salary()

        elif position == 'technician':
            total_salary += Technician(*worker_info).count_salary()
        elif position == 'driver':
            total_salary += Driver(*worker_info).count_salary()

        print(total_salary)
