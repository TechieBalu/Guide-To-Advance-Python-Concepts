from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

# This line is to reduce the number of warning apperaing on the terminal while running the app. 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  
# both below lines used to register the sqlalchemy instance with the flask app. we can use either of it. but using db.init_app has different method
db = SQLAlchemy(app)
# db.init_app(app)

# to create a DB we use db.create_all() function, we can use it in direct or or we can do it with the help of the python terminal 
# by typing the python in the terminal accessing the terminal, importing the "db" from "app" and typing the code 
# db.create_all() 
# this will create the sqlite file in the same directory that we can open it in the DB Browser





class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(50))
    email = db.Column(db.String(100), unique=True)  
    date_joined = db.Column(db.Date, default = datetime.utcnow)
    
    def __repr__(self):
        return f"<User: {self.email}>"

# * Important we cannot create a database just by using the db.create_all() method. because in the 3.0 or above versions are required to 
# go with in the app_context and then use the db.create_all() function

# we use the create_all() functionality to create the database when we use sqlite3 only because using the psotgres, mysql, we need to create
# the database first manually and then create the tables only inside the database. 
# 
# create_all does not update tables if they are already in the database. If you change a model’s columns, use a migration library like 
# Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema. 

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)