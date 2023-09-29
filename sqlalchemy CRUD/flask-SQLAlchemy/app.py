from flask import Flask,redirect,url_for,request,jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import json


app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

# This line is to reduce the number of warning apperaing on the terminal while running the app. 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  
# both below lines used to register the sqlalchemy instance with the flask app. we can use either of it. but using db.init_app has different method
db = SQLAlchemy(app)
# db.init_app(app)



# * Important we cannot create a database just by using the db.create_all() method. because in the 3.0 or above versions 
# of  flask-sqlalchemy are required to go with in the app_context and then use the db.create_all() function



# we use the create_all() functionality to create the database when we use sqlite3 only because using the psotgres, mysql, we need to create
# the database first manually and then create the tables only inside the database. 
# 
# create_all does not update tables if they are already in the database. If you change a model’s columns, use a migration library like 
# Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema. 

# with app.app_context():
#     db.create_all()


@app.route("/add", methods=["POST","GET", "PUT", "DELETE"])
def add_user():
    if request.method == "POST":
        data = request.json
        print(data)

        # response = json.dumps({"ok":"OK"})
        return make_response("OK", 200)


# add_user("Arslan", "arslan@gmail.com")        
# select_all()
# # select_user_by_name_one("Shahmeer")
# select_user_by_name_all("Shahmeer")
# delete(2)
# select_all()
# update(3,"Shahmeer Khan")
# print("\n\n SELECT ALL")
# select_all()



if __name__ == "__main__":
    app.run(debug=True)