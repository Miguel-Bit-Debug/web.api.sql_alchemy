from flask import Blueprint, request

from app.serialize.product_serialize import ProductSchema
from ..services.productService import ProductService

bp_product = Blueprint('product', __name__)

productService = ProductService()

@bp_product.route('/', methods=['GET'])
def index():
    productSchema = ProductSchema(many=True)
    products = productService.listProducts()
    return productSchema.jsonify(products)

@bp_product.route('/<id>', methods=['GET'])
def getById(id: int):
    productSchema = ProductSchema(many=True)
    product = productService.getById(id)
    return productSchema.jsonify(product)

@bp_product.route('/', methods=['POST'])
def add():
    productSchema = ProductSchema()   
    product = productSchema.load(request.json)
    productService.addProduct(product)
    return productSchema.jsonify(product), 201
        
@bp_product.route('/<id>', methods=['PUT'])
def update(id):
    productSchema = ProductSchema()
    product = request.json

    productService.updateService(id, product)
    
    return productSchema.jsonify(product), 200

    
@bp_product.route('/<id>', methods=['DELETE'])
def delete(id):
    productSchema = ProductSchema()

    productService.deleteService(id)
    
    return productSchema.jsonify('delete'), 200