class CityServiceError(Exception):
    service = 'cities'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class CityDoesNotExists(CityServiceError):
    pass


class CityCreationError(CityServiceError):
    pass
