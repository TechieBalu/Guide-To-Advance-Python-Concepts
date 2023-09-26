from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False