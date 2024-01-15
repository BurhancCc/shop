from models.product import ProductModel
from flask import request
from flask_restful import Resource
import os
import json

class Products(Resource):
    
    @classmethod
    def get(cls, id):
        """return all products

        Returns:
            dict: containing all products
        """
        products = ProductModel.find_all(id)
        if products:
            return {'products': [product.json() for product in products]}, 200
        return {'message': 'No products found'}, 404

class FindProduct(Resource):
    
    @classmethod
    def get(cls):
        """return all products if on admin page, else return all products containing search term

        Returns:
            dict: containing all products OR containing all products containing search term
        """
        request.args.get("q")
        searchTerm = request.args.get("q")
        if searchTerm is None:
            products = ProductModel.AllProducts()
            if products:
                return {'products': [product.json() for product in products]}, 200
            return {'message': 'No products found'}, 404
        if searchTerm is not None:
            products = ProductModel.FindProduct(searchTerm)
            if products:
                return {'products': [product.json() for product in products]}, 200
            return {'message': 'No products found'}, 404

    @classmethod
    def post(cls):
        """adds a product to the database if checks are in order and returns a message corresponding to the status

        Returns:
            dict: message corresponding to status
        """
        req_data = request.get_json()
        return ProductModel.RegisterProduct(req_data)