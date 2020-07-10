
class TagsServiceError(Exception):
    service = 'tags'

    def __init__(self, *args):
        super().__init__(self.service, *args)


class TagDoesNotExistsError(TagsServiceError):
    pass


class TagsCreationError(TagsServiceError):
    pass


class TagAdRelationCreationError(TagsServiceError):
    pass
