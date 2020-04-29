class familytree(object):
    def __init__(self, first_name, surname, birthday, baby):
        self.firstname = int(first_name)
        self.surname = int(surname)
        self.birthday = str(birthday)
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
