from app import app
from db import db

db.init_app(app)

#tell sqlalchemy to create a table, use flask-decorator.
@app.before_first_request
def create_table():#before the first request run, it wil run this, which creates this file db.create_all, unless they exist aleady.
    db.create_all()
