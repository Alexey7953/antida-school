from flask.views import MethodView
from flask import Blueprint, jsonify

from src.database import db
from services.colors import ColorService

bp = Blueprint('color', __name__)


class ColorView(MethodView):

    def get(self):
        # Получение списка всех цветов
        with db.connection as connection:
            servies_color = ColorService(connection)
            color = servies_color.read_all_color()
            return jsonify(color), 200


bp.add_url_rule('', view_func=ColorView.as_view('color'))
