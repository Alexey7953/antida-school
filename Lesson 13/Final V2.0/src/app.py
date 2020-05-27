from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Hello, World'
    else:
        return 'This is POST'


app.run()
