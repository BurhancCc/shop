from models.order import OrderModel
from models.order_line import OrderLineModel
from flask import request
from flask_restful import Resource
import os

class PlaceOrder(Resource):

    @classmethod
    def post(cls):
        """places an order and saves it in the database based on the data in <req_data>
        
        Returns:
            int: a HTTP status
        """
        req_data = request.get_json()
        OrderModel.Place(req_data)
        return 200

class GetOrders(Resource):

    @classmethod
    def get(cls):
        """returns all orders placed by customers from the database
        
        Returns:
            list: all orders
        """
        orders = OrderModel.find_all()
        if orders:
            return {"orders": [order.json() for order in orders]}, 200
        return {'message': 'No categories found'}, 404

class ChangeOrderStatus(Resource):

    @classmethod
    def patch(cls, id):
        """changes order status and/or payment status in database for order with ID <id> and returns a message corresponding to the status
        
        Returns:
            dict: message corresponding to status
        """
        req_data = request.get_json()
        return OrderModel.patch(req_data, id)