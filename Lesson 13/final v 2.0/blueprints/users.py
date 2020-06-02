from flask import Blueprint, jsonify, request
from flask.views import MethodView
from werkzeug.security import generate_password_hash

from database import db
from services.users import UsersService

bp = Blueprint('users', __name__)

class UsersView(MethodView):
    def post(self):
        """Регистрация нового пользователя"""
        request_json = request.json

        if not user_request_check(request_json):
            return '', 400
        request_json["password"]= generate_password_hash(request_json["password"])

        with db.connection as connection:
            user_service = UsersService(connection)
            try:
                user_id = user_service.create(user_data=request_json)
            except UserCreationError:
                return '', 409

            user = user_service.read(user_id=user_id)
            user.update({
                "is_seller": request_json["is_seller"],
            })

            if user["is_seller"]:
                seller_service = SellersService(connection)
                zipcode_service = ZipcodesService(connection)
                try:
                    seller_id = seller_service.create(seller_data=request_json, user_id=user_id)
                    zipcode_service.create(zipcode_data=request_json)
                except (SellerCreationError, ZipcodesCreationError):
                    return '', 409

                seller = seller_service.read(seller_id=seller_id)
                user.update(seller)

            return jsonify(user), 201

