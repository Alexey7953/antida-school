from flask import Flask, request, session
from db import get_db, close_db
import requests
from src.database import db

app = Flask(__name__)
app.teardown_appcontext(close_db)


# User registration
@app.route('/users', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        user_id = session.get('user_id')
        if user_id is None:
            return '', 403
        user_json = request.json
        email = user_json.get('email')
        password = user_json.get('password')
        first_name = user_json.get('first_name')
        last_name = user_json.get('last_name')
        is_seller = user_json.get('is_seller')
        phone = user_json.get('phone')
        zip_code = user_json.get('zip_code')
        city_id = user_json.get("city_id")
        street = user_json.get('street')
        home = user_json.get('home')
        return '', 200
    else:
        if request.method == 'GET':
            return '', 200


@app.route('/auth/logout', methods=['POST'])
def logout():
    return '', 401


#
@app.route('/users', methods=['POST'])
def users():
    return '', 201
