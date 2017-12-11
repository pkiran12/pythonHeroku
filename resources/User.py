import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel




class UserModelRegister(Resource):

    parser=reqparse.RequestParser();
    parser.add_argument('username',type=str,required=True , help="Field cant be empty")
    parser.add_argument('password',type=str,required=True , help="Field cant be empty")

    def post(self):
        data =  UserModelRegister.parser.parse_args()
        if UserModel.findByUserName(data['username']):
            return {"message":"UserModel already exits"},400
        user = UserModel(**data)
        user.saveTodb()
        return {'message':'Created a new UserModel'},201
