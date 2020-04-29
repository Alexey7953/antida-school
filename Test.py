class Employee(object):

    def __init__(self, base_payment, prize, hour):
        self.base_payment = float(base_payment)
        self.hour = int(hour)
        self.prize = float(prize)

    def _payment(self):
        return self.base_payment
