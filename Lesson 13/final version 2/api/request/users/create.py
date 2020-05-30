from marshmallow import Schema, fields
from ...base import RequestModel


class RequestCreateUserSchema(Schema):
    first_name = fields.Str(required=False, allow_none=True)
    last_name = fields.Str(required=False, allow_none=True)
    is_seller = fields.Bool(required=False, allow_none=True)
    phone = fields.Str(required=False, allow_none=True)
    zip_code = fields.Int(required=False, allow_none=True)
    city_id = fields.Int(required=False, allow_none=True)
    street = fields.Str(required=False, allow_none=True)
    home = fields.Str(required=False, allow_none=True)


class RequestCreateUser(RequestModel, RequestCreateUserSchema):
    __schema__ = RequestCreateUserSchema
