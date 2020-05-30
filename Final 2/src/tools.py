from functools import wraps

from flask import session

from services.users import (
    UsersService,
    UserDoesNotExistsError,
)
from services.sellers import (
    SellersService,
    SellerDoesNotExistsError,
)
from src.database import db


def user_request_check(request_json) -> bool:
    if not all([
        request_json.get('email'),
        request_json.get('password'),
        request_json.get('first_name'),
        request_json.get('last_name'),
    ]):
        return False

    if request_json.get('is_seller') and not all([
        request_json.get('phone'),
        request_json.get('zip_code'),
        request_json.get('city_id'),
        request_json.get('street'),
        request_json.get('home'),
    ]):
        return False

    return True


def auth_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        user_id = session.get("user_id")
        if not user_id:
            return '', 403

        with db.connection as connection:

            user_service = UsersService(connection)
            try:
                user = user_service.read(user_id)
            except UserDoesNotExistsError:
                return '', 403

            return func(*args, **kwargs, user=user)
    return wrapper


def seller_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        with db.connection as connection:
            seller_service = SellersService(connection)
            try:
                seller_service.get_id(user_id=kwargs["user"].get("id"))
            except SellerDoesNotExistsError:
                return '', 403

        return func(*args, **kwargs)
    return wrapper
