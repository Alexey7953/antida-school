class AdsServiceError(Exception):
    service = 'ads'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class AdsCreationError(AdsServiceError):
    pass


class AdsUpdateError(AdsServiceError):
    pass


class AdsDeleteError(AdsServiceError):
    pass


class AdDoesNotExists(AdsServiceError):
    pass
