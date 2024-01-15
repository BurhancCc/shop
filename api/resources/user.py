from models.user import UserModel
from models.order import OrderModel
from models.order_line import OrderLineModel
from flask import request
from flask_restful import Resource
import os
import re
from flask_jwt import JWT, jwt_required, current_identity

class RegisterUser(Resource):

    @classmethod
    def post(cls):
        """registers a user to the database according to <req_data> after performing checks and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        req_data = request.get_json()
        return UserModel.Register(req_data)

class loginNaam(Resource):
    """[LoginName]

    Args:
        Resource Used for endpoint: necessary for getting users logged in.

    Returns:
        [json]: [current logged in user]
    """
    @classmethod
    @jwt_required()
    def get(cls):
        huidige_gebruiker = current_identity.json()
        return huidige_gebruiker

class GetOrder(Resource):
    
    @classmethod
    def get(cls, id):
        """returns orders placed by customer with ID <id> from the database
        
        Returns:
            list: multiple orders from single customer
        """
        orders = OrderModel.get(id)
        if orders:
            return {'orders': [order.json() for order in orders]}, 200
        return {'message': 'No orders found'}, 404

class EditUser(Resource):

    @classmethod
    def patch(cls, id):
        """updates user ID'd <id> in the database according to <req_data> after performing checks and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        req_data = request.get_json()
        return UserModel.patch(req_data, id)