class CarsServiceError(Exception):
    service = 'cars'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class CarCreationError(CarsServiceError):
    pass


class CarDeleteError(CarsServiceError):
    pass


class CarDoesNotExists(CarsServiceError):
    pass
