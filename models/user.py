from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):#remove id, id is autoincrement, don't need id.
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    #we are not using self, instead, we are usig class
    @classmethod #use cls, instead of hard coded class name
    def find_by_username(cls, username):#self - every object needs to interact with object type users
        return cls.query.filter_by(username = username).first()#first username is the col name in the table, and the 2nd username is the argumnet name

    @classmethod #use cls, instead of hard coded class name
    def find_by_id(cls, _id):#self - every object needs to interact with object type users
        return cls.query.filter_by(id = _id).first()
