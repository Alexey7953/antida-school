from src import app


if __name__ == '__main__':
    app = app.create_app()
    app.run(
        host='127.0.0.1',
        port='5000',
        debug=True,
    )