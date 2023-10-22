import datetime

from flask_sqlalchemy import  SQLAlchemy
# from flask_sqlalchemy import func
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ ='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now())
