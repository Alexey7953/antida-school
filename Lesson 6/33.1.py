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


# Оптимальное решение
"""
# Базовый класс, куда мы вынесли общее для ВСЕХ работников
# состояние (зарплата и премия) и поведение (вычисление полной зарплаты).
class Employee:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    # Так как премия является фиксированной надбавкой к базовой зарплате,
    # разобьем логику вычисления на 2 метода.
    # Метод compute_base_salary вычисляет базовую зарплату.
    # В данном классе он не реализован, так как нет общей логики для всех работников,
    # но именно этот метод будет переопределяться в наследниках.
    def compute_base_salary(self):
        raise NotImplementedError

    # Метод compute_full_salary вычисляет зарплату с учетом премии,
    # получая базовую часть из метода compute_base_salary.
    # В дочерних классах перегружать данный метод не требуется.
    def compute_full_salary(self):
        return self.compute_base_salary() + self.bonus


class MonthlyPaidEmployee(Employee):
    def compute_base_salary(self):
        return self.salary


class HourlyPaidEmployee(Employee):
    # В конструкторе добавляется спицифичный для работников с почасовой зарплатой
    # атрибут hours_worked.
    # Остальные параметры передаются базовому конструктору как есть.
    def __init__(self, salary, bonus, hours_worked):
        super().__init__(salary, bonus)
        self.hours_worked = hours_worked

    def compute_base_salary(self):
        return self.salary * self.hours_worked


# Класс, реализующий логику работников с категориями.
# Пердполагается, что этот класс будет использоваться в комбинации
# с MonthlyPaidEmployee или HourlyPaidEmployee.
class RankedEmployee(Employee):
    categories = {
        'A': 1.25,
        'B': 1.15,
        'C': 1.00,
    }

    # Так как мы не знаем, от какого из двух классов наследуется,
    # то принимаем любые атрибуты и предаем их как есть базовому конструктору.
    # Кроме того, сохраняем категорию работника.
    def __init__(self, category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = category

    # Вычисляем базовую зарплату, делигируя вызов базовому классу
    # и домножаем на коеффициент категории.
    def compute_base_salary(self):
        base_salary = super().compute_base_salary()
        category_factor = self.categories[self.category]
        return base_salary * category_factor


class Manager(MonthlyPaidEmployee):
    pass


# Используем мнодественное наследование, чтобы скомбинировать логику вычисления зарплаты.
# Согласно MRO цепочка вызовов будет следующей:
#   1. Technician.compute_full_salary
#   2. Technician.compute_base_salary
#   3. RankedEmployee.compute_base_salary
#   4. MonthlyPaidEmployee.compute_base_salary
class Technician(RankedEmployee, MonthlyPaidEmployee):
    pass


# Используем мнодественное наследование, чтобы скомбинировать логику вычисления зарплаты.
# Согласно MRO цепочка вызовов будет следующей:
#   1. Driver.compute_full_salary
#   2. Driver.compute_base_salary
#   3. RankedEmployee.compute_base_salary
#   4. HourlyPaidEmployee.compute_base_salary
class Driver(RankedEmployee, HourlyPaidEmployee):
    pass


def main():
    n = int(input())
    total_salary = 0

    for _ in range(n):
        # Так как последний параметр опциональный, используем запаковку *
        # Приводим значения к нужным типам.
        profession, salary, bonus, hours_worked, *category = input().split()
        salary = float(salary)
        bonus = float(bonus)
        hours_worked = int(hours_worked)

        # Не будем усложнять создание экземпляров,
        # используем простой условный оператор.
        if profession == 'manager':
            employee = Manager(salary, bonus)
        elif profession == 'technician':
            employee = Technician(*category, salary, bonus)
        elif profession == 'driver':
            employee = Driver(*category, salary, bonus, hours_worked)

        total_salary += employee.compute_full_salary()

    print(total_salary)


if __name__ == '__main__':
    main()
"""