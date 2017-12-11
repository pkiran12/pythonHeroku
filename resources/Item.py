
from flask_restful import Resource,reqparse,Api
from flask_jwt import jwt_required
from models.item import ItemModel


#jwt json token encoded
class Item(Resource):

    parser=reqparse.RequestParser();
    parser.add_argument('quantity',type=float,required=True , help="Field cant be empty")
    parser.add_argument('price',type=float,required=True , help="Field cant be empty")
    parser.add_argument('store_id',type=int,required=True , help="Field cant be empty")
      #data=request.get_json(silent=True)
    #data=parser.parse_args()

    @jwt_required()
    def get(Self, name):

        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}
	#	if itemList.len !=0 :
		#	return itemList[0]





    def post(self,name):
         #data =request.get_json(force=True) ## Doesnt check the header and avoid using
         #data=request.get_json(silent=True) # Doesnt do anything to give error

         #data=request.get_json(silent=True)

         if ItemModel.find_by_name(name):
             return {'message': "An item with {} name already exists".format(name)}, 400

         data=Item.parser.parse_args()
         #item={'name':name,'price':data['price'],'quantity': data['quantity']}
         #item = ItemModel(name,data['price'],data['quantity'],data['store_id'])
         item = ItemModel(name,**data)

         try:
             item.save_to_db()
         except Exception as e:
             return{"message":"Error occured while storing the item into database . Reason {}".format(e)},500#interval serveer error
         return item.json(),201





    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.deleteFromDB()
        return {'message':'item deleted'}

    def put(self,name):

        #parser.add_argument('price',type=float,required=True , help="Field cant be empty")
        #data=request.get_json(silent=True)
        data=Item.parser.parse_args()
        #item=next(filter(lambda x:x['name']==name,items),None)
        item =ItemModel.find_by_name(name)
        #updated_item={'name':name,'price':data['price'],'quantity': data['quantity']}
#        updated_item=ItemModel(name,data['price'],data['quantity'])
        if item is None:
            #item = ItemModel(name,data['price'],data['quantity'],data['store_id'])
            item  = ItemModel(name,**data)
        else:
            item.price=data['price']
            item.quantity=data['quantity']
            item.store_id=data['store_id']
        item.save_to_db()
        return item.json()

class Itemlist(Resource):
    """Items list data for the source"""
    def get(self):
        #Item model to return all the models
         #return {'items':[item.json() for all in ItemModel.query.all()]}
         return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}



#api.add_resource(Item,'/item/<string:name>')
#api.add_resource(Itemlist,'/items')
