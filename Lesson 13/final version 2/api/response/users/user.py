from marshmallow import Schema, fields

from api.base import ResponseModel


class ResponseUserSchema(Schema):
    first_name = fields.Str(required=False, allow_none=True)
    last_name = fields.Str(required=False, allow_none=True)
    is_seller = fields.Bool(required=False, allow_none=True)
    phone = fields.Str(required=False, allow_none=True)
    zip_code = fields.Int(required=False, allow_none=True)
    city_id = fields.Int(required=False, allow_none=True)
    street = fields.Str(required=False, allow_none=True)
    home = fields.Str(required=False, allow_none=True)


class ResponseUser(ResponseModel):
    __schema__ = ResponseUserSchema
