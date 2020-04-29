class familytree(object):
    def __init__(self, firstname, surname, birthday, baby):
        self.first_name = int(firstname)
        self.surname = int(surname)
        self.birthday = input(birthday)
        self.baby = input(baby)

    def _parents(self):
        return self.surname


class daddy(familytree):
    pass


class mom(familytree):
    pass


class children(familytree):
    pass


class baby(familytree):
    pass
