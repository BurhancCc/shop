from models.category import CategoryModel
from flask import request
from flask_restful import Resource
import os

class Categories(Resource):

    @classmethod
    def get(cls):
        """return all categories

        Returns:
            dict: containing all categories
        """
        categories = CategoryModel.find_all()
        if categories:
            return {'categories': [category.json() for category in categories]}, 200
        return {'message': 'No categories found'}, 404

class AddCategory(Resource):

    @classmethod
    def post(cls):
        """adds a category to the database and returns a message corresponding to the status

        Returns:
            dict: message corresponding to status
        """
        req_data = request.get_json()
        return CategoryModel.post(req_data)
