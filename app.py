import os

from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from Security import authenticate, identity
from resources.User import UserModelRegister
from resources.Item import Item, Itemlist
from resources.store import Store,StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'jose'
api = Api(app)




jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserModelRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/storelist')

if __name__ == '__main__':
    from db import db # importing the db to avoid circular imports
    db.init_app(app)
    app.run(port=5432,debug=True)
