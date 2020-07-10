class ImageServiceError(Exception):
    service = 'image'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class ImageServiceError(ImageServiceError):
    pass


class ImageUpdateError(ImageServiceError):
    pass
