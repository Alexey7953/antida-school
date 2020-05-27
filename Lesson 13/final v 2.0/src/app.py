from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return '\n'.join(
            f'{key}: {value}'
            for key, value in request.args.items()
        )
    else:
        return '\n'.join(
            f'{key}: {value}'
            for key, value in request.args.items()
        )


app.debug = True
app.run()
