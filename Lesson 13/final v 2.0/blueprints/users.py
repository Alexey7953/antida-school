from flask import Blueprint, jsonify, request
from flask.views import MethodView

bp = Blueprint('users', __name__)

class UsersView(MethodView):
    def post(self):
        """Регистрация нового пользователя"""
        request_json = request.json

        if not user_request_check(request_json):
            return '', 400
