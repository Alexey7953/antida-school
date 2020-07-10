class ColorServiceError(Exception):
    service = 'color'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class ColorCreationError(ColorServiceError):
    pass


class ColorDoesNotExists(ColorServiceError):
    pass


class CarColorRelationCreationError(ColorServiceError):
    pass