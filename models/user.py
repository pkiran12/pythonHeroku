import sqlite3
from db import db
#model represtation of internal entity
#Respurce is a external respresentation of entity

class UserModel(db.Model):
    __tablename__='users'


    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100)) # limiting the size of the characters
    password = db.Column(db.String(100))


    def __init__(self,username,password):
        
        self.username=username
        self.password=password

    def saveTodb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findByUserName(cls,username):
        return cls.query.filter_by(username=username).first()



    @classmethod
    def findById(cls,_id):
        return cls.query.filter_by(id=_id).first()
