from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT
from Security import authenticate,identity
from User import UserRegister
from Item import Item,Itemlist

app=Flask(__name__)
api=Api(app)
app.secret_key='kiran'

jwt=JWT(app,authenticate,identity) #/auth creates a new end point

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5432,debug=True)
