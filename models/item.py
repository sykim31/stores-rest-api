from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2)) #currency is usually 2

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):#object property, internal representation.
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):#return json representation of the model (i.e., dictionary)
        return {'name': self.name, 'price':self.price}

    #move all the methods from the item resources that don't belong to item model.
    @classmethod
    def find_by_name(cls, name):#still class, because it returs an object.
        return cls.query.filter_by(name=name).first()#equivalent .to "select * from items where name= name limit 1

    def save_to_db(self): #both insert and update
        db.session.add(self)#session - collection of objects
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
