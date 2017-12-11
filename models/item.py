import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__='items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100)) # limiting the size of the characters
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer)

    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    store=db.relationship('StoreModel')


    def __init__(self,name,price,quantity,store_id):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.store_id=store_id


    def json(self):
        return {'name':self.name,'price':self.price,"quantity":self.quantity}

    @classmethod
    def find_by_name(cls,name):
        return ItemModel.query.filter_by(name=name).first() # Select * from items where name=name returns the first row only



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete(cls,item):
         connection=sqlite3.connect('mydatabase.db')
         cursor=connection.cursor()
         query = "Delete from items where name=?"
         cursor.execute(query,(name,))
         connection.commit()
         connection.close()

    @classmethod
    def delete(cls,item):
         connection=sqlite3.connect('mydatabase.db')
         cursor=connection.cursor()
         query = "Delete from items where name=?"
         cursor.execute(query,(name,))
         connection.commit()
         connection.close()

    @classmethod
    def getAllItems(cls):
         connection=sqlite3.connect('mydatabase.db')
         cursor=connection.cursor()
         query = "Select *from items"
         result = cursor.execute(query)
         items=[]
         for row in result:
             items.append({'name':row[0],'price':row[1],'quantity':row[2]});
         connection.commit()
         connection.close()
         return items
