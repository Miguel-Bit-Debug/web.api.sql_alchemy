from ..db.db_config import db

database = db

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(200))
    description = database.Column(database.String(200))