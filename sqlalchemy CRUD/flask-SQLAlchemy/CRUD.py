from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from app import app , db
from models import User


def select_all():
    print("IM IN SELECT ALL")
    # selectQuery = User.query.all()
    # print(selectQuery)
    # selectQuery = db.select(User).scalars()
    with app.app_context():
        selectQuery = User.query.all()
    #     selectQuery = db.session.execute(db.select(User).order_by(User.name)).all()
        # print(selectQuery)
        # print(type(selectQuery[0]))
        # print(selectQuery[0].id)

        data = []
        for i in selectQuery:
            data.append({"name":i.name, "email":i.email})
        
        # print(data)

        return data
            

select_all()
# INSERT:
def add_user(name,email):
        print("IM IN ADD USER")
        user = User(name = name, email = email)
        with app.app_context():
            try:
                db.session.add(user)
                db.session.commit()
                return True
            except IntegrityError as e :
                db.session.rollback()  # Rollback the transaction to avoid leaving the database in an inconsistent state
                print(f"IntegrityError: {str(e)}")
                return {"error":"Email Already Exists"}
            
            # finally:
            #     db.session.close()

def select_user_by_name_one(name):
    with app.app_context():
        user = db.session.execute(db.select(User).filter_by(name=name)).scalar_one()
        print(user)
        print("ID of User is: ", user.id)
        print("Name of User is: ", user.name)

    
    return user

def select_user_by_id(id):
    with app.app_context():
        user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
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