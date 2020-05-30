from typing import Dict


class RequestModel:
    __schema__ = None

    def __init__(self, params: dict):
        self._import(params)
        self._validate(params)
        pass

    def _import(self, params: dict):
        for k, v in params.items():
            setattr(self, k, v)

    def _validate(self, params: dict):
        schema = self.__schema__()
        errors = schema.validate(params)
        self._raise_errors(errors)

    @staticmethod
    def _raise_errors(errors: Dict[str, list]):
        if len(errors) == 0:
            return

        for field in errors:
            error_message = errors[field]

            if isinstance(error_message, list):
                if len(error_message) != 0:
                    error_message = error_message[0]
                else:
                    error_message = None

            if error_message is None:
                continue

            raise Exception(f'Field: {field}, error_massage: {error_message}')


class ResponseModel:
    __schema__ = None

    def __init__(self, obj: object):
        properties = [pr for pr in dir(obj) if not pr.startswith('_')]

        for property in properties:
            if property[:1] == '_':
                continue

            self._import_field(obj, property)

    def _import_field(self, source_obj: object, name: str):
        value = source_obj.__getattribute__(name)

        if not callable(value):
            setattr(self, name, value)

    def data(self):
        result = self.__schema__().dump(self)
        return result
