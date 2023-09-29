from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

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
        return f"<User: {self.email}, Name: {self.name}>"

# * Important we cannot create a database just by using the db.create_all() method. because in the 3.0 or above versions are required to 
# go with in the app_context and then use the db.create_all() function

# we use the create_all() functionality to create the database when we use sqlite3 only because using the psotgres, mysql, we need to create
# the database first manually and then create the tables only inside the database. 
# 
# create_all does not update tables if they are already in the database. If you change a model’s columns, use a migration library like 
# Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema. 

with app.app_context():
    db.create_all()


def select_all():
    # selectQuery = User.query.all()
    
    # selectQuery = db.select(User).scalars()
    with app.app_context():
        selectQuery = db.session.execute(db.select(User).order_by(User.name)).scalars()
        print(selectQuery.all())


# INSERT:
def add_user(name,email):
    
        user = User(name = name, email = email)
        with app.app_context():
            try:
                db.session.add(user)
                db.session.commit()
            except IntegrityError as e :
                db.session.rollback()  # Rollback the transaction to avoid leaving the database in an inconsistent state
                print(f"IntegrityError: {str(e)}")
            
            # finally:
            #     db.session.close()

def select_user_by_name_one(name):
    with app.app_context():
        user = db.session.execute(db.select(User).filter_by(name=name)).scalar_one()
        print(user)
        print("ID of User is: ", user.id)
        print("Name of User is: ", user.name)

    
    return user

def select_user_by_name_all(name):
    with app.app_context():
        user = db.session.execute(db.select(User).filter_by(name=name)).scalars()
        print("\n User is: ",user)
        for us in user:
            print(us)
            print("ID of User is: ", us.id)
            print("Name of User is: ", us.name, "\n\n")

    
    return user

def delete(id):
    with app.app_context():
        user = db.session.get(User,id)
        # print(user)
        if user is not None:
            db.session.delete(user)
            db.session.commit()


def update(id, name):
    with app.app_context():
        user = db.session.get(User,id)
        if user is not None:
            user.name = name
            db.session.commit()

add_user("Arslan", "arslan@gmail.com")        
select_all()
# select_user_by_name_one("Shahmeer")
select_user_by_name_all("Shahmeer")
delete(2)
select_all()
update(3,"Shahmeer Khan")
print("\n\n SELECT ALL")
select_all()



if __name__ == "__main__":
    app.run(debug=True)