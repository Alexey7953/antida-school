from flask import Blueprint, request
from flask.views import MethodView
from api.request.users import RequestCreateUser
from api.response.users.user import ResponseUser
from db.models.users import DBUser, DBUserWithCity
from db.connection import db

bp = Blueprint('users', __name__)


class UsersView(MethodView):

    def post(self):
        session = db.make_session()

        request_model = RequestCreateUser(request.json)

        db_user = DBUser(
            first_name=request_model.first_name if hasattr(request_model, 'first_name') else None,
            last_name=request_model.last_name if hasattr(request_model, 'last_name') else None,
            is_seller=request_model.is_seller if hasattr(request_model, 'is_seller') else None,
            phone=request_model.phone if hasattr(request_model, 'phone') else None,
            zip_code=request_model.zip_code if hasattr(request_model, 'zip_code') else None,
            # city_id=request_model.city_id if hasattr(request_model, 'city_id') else None,
            street=request_model.street if hasattr(request_model, 'street') else None,
            home=request_model.home if hasattr(request_model, 'home') else None
        )

        session.add_model(db_user)
        session.commit_session()

        user_with_id = session.query(DBUserWithCity).filter(DBUserWithCity.id == 3).one()
        response = ResponseUser(db_user)

        j = response.data()
        return j

bp.add_url_rule('', view_func=UsersView.as_view('users'))
