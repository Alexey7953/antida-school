from flask import (
    Blueprint,
    request,
    jsonify
)

from flask.views import MethodView

from services.cities import (
    CitiesService,
    CityCreationError,
    CityDoesNotExists
)

from src.database import db

bp = Blueprint('cities', __name__)


class CitiesView(MethodView):
    # Получение списка всех городов
    def get(self):
        with db.connection as connection:
            service = CitiesService(connection)
            cities = service.read_all()
            return jsonify(cities), 200

    def post(self):
        # Создание нового города

        name = request.json.get("name")

        with db.connection as connection:
            service = CitiesService(connection)

            try:
                city = service.read(name)
            except CityDoesNotExists:
                service.create(name)
                city = service.read(name)
            except CityCreationError:
                return '', 500

            return jsonify(city), 200


bp.add_url_rule('', view_func=CitiesView.as_view('cities'))
