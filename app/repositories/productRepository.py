from app.models.product import Product
from ..db import db_config

class ProductRepository:
    def __init__(self):
        self.__product = Product()
        self.__db = db_config.db

    def listProduct(self):
        products = self.__product.query.all()
        self.__db.session.close()
        return products

    def addProduct(self, product):
        self.__db.session.add(product)
        self.__db.session.commit()
        self.__db.session.close()
    
    def getById(self, id):
        product = self.__product.query.filter_by(id=id)
        self.__db.session.close()
        return  product

    def updateProduct(self, id, product):
        oldProduct = self.__product.query.filter_by(id=id)

        print(oldProduct)

        
        oldProduct.update(product)
        self.__db.session.commit()
        self.__db.session.close()

    def deleteProduct(self, id):
        self.__product.query.filter_by(id=id).delete()
        self.__db.session.commit()
        self.__db.session.close()
