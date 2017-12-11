import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__='stores'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100)) # limiting the size of the characters
    items = db.relationship('ItemModel',lazy='dynamic') # doesnt create an item entry for each Model that mathces store id

    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]} # self.items reads the list of items its a query builder and all is used to retrive all the item in the table

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() # Select * from items where name=name returns the first row only

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
