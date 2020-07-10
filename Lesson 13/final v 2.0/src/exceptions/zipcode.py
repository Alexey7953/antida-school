class ZipcodesServiceError(Exception):
    service = 'zip_code'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class Zip_codesCreationError(ZipcodesServiceError):
    pass


class Zip_codesUpdateError(ZipcodesServiceError):
    pass


class Zip_codesCreationError(ZipcodesServiceError):
    pass
