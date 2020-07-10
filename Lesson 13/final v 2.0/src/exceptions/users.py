class UsersServiceError(Exception):
    service = 'users'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class UserDoesNotExistsError(UsersServiceError):
    pass


class UserCreationError(UsersServiceError):
    pass


class UserUpdateError(UsersServiceError):
    pass
