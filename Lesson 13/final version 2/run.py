from flask import Flask
from sqlalchemy import create_engine

from blueprints.users import bp as users_bp
from db.connection import DataBase

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(users_bp, url_prefix='/users')

    app.run(
        host='127.0.0.1',
        port='8082',
        debug=True
    )
