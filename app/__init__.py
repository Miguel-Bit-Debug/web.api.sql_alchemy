from flask import Flask
from .routes.product import bp_product
from .db.db_config import config_db
from .serialize.product_serialize import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mssql://LAPTOP-65C1BIEB\SQLEXPRESS/FLASK_API?trusted_connection=yes&driver=SQL+Server"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    app.register_blueprint(bp_product)
    
    return app
