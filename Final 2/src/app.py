from flask import Flask

from blueprints.cities import bp as cities_bp

from src.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(cities_bp, url_prefix='/cities')

    db.init_app(app)
    return app


