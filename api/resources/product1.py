from models.product1 import oneProductModel
from flask import request
from flask_restful import Resource
import os

class Product(Resource):
    
    @classmethod
    def get(cls, id):
        """returns a single product with id <id> from the database

        Returns:
            list: a single product
        """
        product = oneProductModel.find(id)
        if product:
            return product.json(), 200
        return {'message': 'No product found'}, 404

class EditProduct(Resource):

    @classmethod
    def patch(cls, id):
        """performs checks and if all correct edits product ID'd <id> in the database according to <req_data> and returns a message corresponding to status
        
        Returns:
            dict: message corresponding to status
        """
        req_data = request.get_json()
        return oneProductModel.patch(req_data, id)

class RemoveProduct(Resource):

    @classmethod
    def delete(cls, id):
        """deletes a single product with id <id> from the database if it's not part of an unshipped/unpaid order and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        return oneProductModel.delete(id)