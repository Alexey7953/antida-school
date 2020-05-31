from flask import Flask
from src.db import close_db
from src.database import db
from blueprints.cities import bp as bp_cities
from blueprints.colors import bp as bp_color
from blueprints.image import bp as bp_image


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.teardown_appcontext(close_db)
    app.register_blueprint(bp_color, url_prefix='/color')
    app.register_blueprint(bp_cities, url_prefix='/cities')
    app.register_blueprint(bp_image, url_prefix='/image')
    db.init_app(app)
    return app
