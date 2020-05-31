from flask import Flask
from src.db import close_db

app = Flask(__name__)
app.teardown_appcontext(close_db)

app.debug = True
app.run()
