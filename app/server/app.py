from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object("server.config.Config")
db = SQLAlchemy(app)


@app.route("/")
def home():
    return "Hola mundo"
