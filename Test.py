


class Worker(object):

    def __init__(self, base_payment, prize, hours):
        self.base_payment = float(base_payment)
        self.prize = float(prize)
        self.hours = int(hours)

    def _payment(self) -> float:
        return self.base_payment

    def count_salary(self) -> float:
        return self._payment() + self.prize


class WorkerWithCategory(Worker):

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


class WorkerRateByHours(Worker):
    """Класс сотрудников организации с почасовой ставкой"""

    def _payment(self):
        return super()._payment() * self.hours


class Manager(Worker):
    """Класс менеджера"""
    pass


class Technician(WorkerWithCategory):
    """Класс техника"""
    pass


class Driver(WorkerRateByHours, WorkerWithCategory):
    """Класс водителя"""
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