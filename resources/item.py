from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()#parser belongs to class, not a specific item (there is no self)
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'This field cannot be left blank!'
        )

    parser.add_argument(
        'store_id',
        type = int,
        required = True,
        help = 'Every Item needs a store id'
        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()#return item dictionary, not object itself.
        return {'message': 'item not found.'}, 404


    def post(self, name):
        #first deal with errors.
        if ItemModel.find_by_name(name):#we returns object, cannot return item dictioary.
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        #if there is no error, load the data.
        data = Item.parser.parse_args()

        #item = {'name': name, 'price':data['price']}#this is a dictionary, but should return item model object.
        item = ItemModel(name, data['price'], data['store_id'])
        #item = ItemModel(name, *data) maybe two **data

        try:
            #ItemModel.insert(item)
            item.save_to_db()#insert item itself, does not need to call class needlessly.
        except:
            return {'message':'an error occurred inserting the item'}, 500#internal server error

        return item.json(), 201#we always have to return json.

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'Item deleted'}

    def put (self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item = ItemModel(name, data['price'], data['store_id'])#need to check. the class script use item.price = data['price']
            #item = ItemModel(name, **data)
            #item.price = data['price']
        else:#if the item already exists, then updte the dictionary
            item = ItemModel(name, data['price'], data['store_id'])#need to check the class script use item = ItemModel(name, data['price'])

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        #return {'items':[item.json() for item in ItemModel.query.all()]}#use list comprehension to return all items.more pythonic
        return {'items': list(map(lambda x:x.json(), ItemModel.query.all()))} #those who work on other languages easy to understand
