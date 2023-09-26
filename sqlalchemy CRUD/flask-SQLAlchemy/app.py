from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# This line is to reduce the number of warning apperaing on the terminal while running the app. 
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# both below lines used to register the sqlalchemy instance with the flask app. we can use either of it. but using db.init_app has different method
db = SQLAlchemy(app)
# db.init_app(app)

# to create a DB we use db.create_all() function, we can use it in direct or or we can do it with the help of the python terminal 
# by typing the python in the terminal accessing the terminal, importing the "db" from "app" and typing the code 
# db.create_all() 
# this will create the sqlite file in the same directory that we can open it in the DB Browser
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)