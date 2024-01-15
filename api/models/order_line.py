import sqlite3
import os
import json
from flask import request
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from models.product1 import oneProductModel

class OrderLineModel:
    
    def __init__(self, id, product, order, amount, total_price):
        """OrderLineModel constructor

        Args:
            id (int): database id
            product (int): product id
            order (int): order id
            amount (int):
            total_price (int): in cents
        """
        self.id = id
        self.product = product
        self.order = order
        self.amount = amount
        self.total_price = total_price

    @classmethod
    def get(cls, id):
        """returns a single orderline with id <id> from the database
        
        Returns:
            list: a single orderline
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM order_lines WHERE order_id=" + str(id) + " ORDER BY id")
        rows = cur.fetchall()
        conn.close()
        orderLines = list()
        for row in rows:
            product = oneProductModel.find(row[1])
            orderLines.append(OrderLineModel(row[0], product.json(), row[2], row[3], row[4]).json())
        return orderLines


    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__