from datetime import datetime
from flask import Blueprint, jsonify, request
from flask.views import MethodView

from database import db
from services.ads import AdsService
from services.cars import CarsService
from services.colors import ColorService
from services.image import ImageService
from services.tags import TagsService

bp = Blueprint('ads', __name__)


def generation_ad_dict(ad_id: int) -> dict:
    """Формирование словаря представления объявления"""
    with db.connection as connection:
        ad_service = AdsService(connection)
        response = ad_service.read_ad(ad_id)

        car_service = CarsService(connection)
        response["car"] = car_service.read_car(ad_id=ad_id)

        color_service = ColorService(connection)
        response["car"]["colors"] = color_service.read_color(ad_id=ad_id)

        image_service = ImageService(connection)
        response["car"]["images"] = image_service.read_image(ad_id=ad_id)

        tags_service = TagsService(connection)
        response["tags"] = tags_service.read_tag(ad_id=ad_id)
    return response


class AdsView(MethodView):
    def get(self):
        """Получение списка объявлений"""
        




