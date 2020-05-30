
from flask import Flask
from

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(cities_bp, url_prefix='/users')

    db.init_app(app)

    app.run(
        host='127.0.0.1',
        port='5000',
        debug=True,
    )
