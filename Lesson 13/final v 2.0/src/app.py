from flask import Flask, request
from db import get_db, close_db
import requests

app = Flask(__name__)
app.teardown_appcontext(close_db)


# Authorization: input and output
@app.route('/auth/login', methods=['POST'])
def login():
    request_json = request.json
    email = request_json.get('email')
    password = request_json.get('password')

    return '', 200


@app.route('/users', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
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


# User registration
@app.route('/users', methods=['POST'])
def users():
    return '', 201


# Create city
@app.route('/cities', methods=['POST', "GET"])
def cities():
    if request.method == 'POST':
        cities_json = request.json
        name = cities_json.get('name')
        return f'{name}', 201
    else:
        return '', 405


app.debug = True
app.run()
