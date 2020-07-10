class SellerServiceError(Exception):
    service = 'sellers'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class SellerDoesNotExistsError(SellerServiceError):
    pass


class SellerCreationError(SellerServiceError):
    pass


class SellerBadRequest(SellerServiceError):
    pass


class SellerUpdateError(SellerServiceError):
    pass


class SellerDeleteError(SellerServiceError):
    pass
