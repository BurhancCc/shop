from models.country import CountryModel
from flask import request
from flask_restful import Resource
import os

class Countries(Resource):
    
    @classmethod
    def get(cls):
        """return all countries

        Returns:
            dict: containing all countries
        """
        countries = CountryModel.find_all()
        if countries:
            return {'countries': [country.json() for country in countries]}, 200
        return {'message': 'No countries found'}, 404

class AddCountry(Resource):

    @classmethod
    def post(cls):
        """adds a country to the database and return a message corresponding to the status

        Returns:
            dict: message corresponding to status
        """
        req_data = request.get_json()
        return CountryModel.post(req_data)
