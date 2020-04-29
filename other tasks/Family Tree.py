class familytree(object):
    def __init__(self, first_name, last_name, birthday):
        self.first_name = int(first_name)
        self.last_name = int(last_name)
        self.birthday = input(birthday)

class daddy(familytree):
    pass
class mom(familytree):
    pass
class children(familytree):
    pass