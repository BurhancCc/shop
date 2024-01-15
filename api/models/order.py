import sqlite3
import os
import json
from flask import request
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from datetime import datetime
from models.user import UserModel
from models.order_line import OrderLineModel
from itertools import chain

class OrderModel:
    
    def __init__(self, id, date, paid, shipped, user, order_lines):
        """OrderModel constructor

        Args:
            id (int): database id
            date (string): 
            paid (int): 0 for no, 1 for yes
            shipped (int): 0 for no, 1 for yes
            user (int): user id
        """
        self.id = id
        self.date = date
        self.paid = paid
        self.shipped = shipped
        self.user = user
        self.order_lines = order_lines

    
    @classmethod
    @jwt_required()
    def Place(cls, req_data):
        """places an order and saves it in the database based on the data in <req_data>
        
        Returns:
            int: a HTTP status
        """
        huidige_gebruiker = current_identity.json()
        userID = huidige_gebruiker["id"]
        conn = sqlite3.connect('db/webshop.db')
        cur = conn.cursor()
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d %H:%M:%S")
        notPaid = 0
        notShipped = 0
        cur.execute('''INSERT INTO orders(date, paid, shipped, user_id)
            VALUES (?,?,?,?)''',(dt_string, notPaid, notShipped, userID))
        products = []
        amounts = []
        prices = []
        vat = 1.21
        for i in range(len(req_data["lines"])):
            products.append(req_data["lines"][i]['product'])
            amounts.append(req_data["lines"][i]['amount'])
        cur.execute("SELECT MAX(id) FROM orders")
        orderId = cur.fetchall()

        for i in range(len(products)):
            cur.execute("SELECT price FROM products WHERE id=" + (str(products[i])))
            prices.append(cur.fetchall())

        for i in range(len(products)):
            totalPrice = (prices[i][0][0] * amounts[i] * vat)
            cur.execute('''INSERT INTO order_lines(product, order_id, amount, total_price)
                VALUES (?,?,?,?)''',(products[i], orderId[0][0], amounts[i], totalPrice))
        conn.commit()
        conn.close()
        return 200
    
    @classmethod
    def get(cls, id):
        """returns orders placed by customer with ID <id> from the database
        
        Returns:
            list: multiple orders from single customer
        """
        conn = sqlite3.connect('db/webshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM orders WHERE user_id=' + str(id) + " ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()
        orders = list()
        for row in rows:
            user = UserModel.find(row[4])
            orders.append(OrderModel(row[0], row[1], row[2], row[3], user.json(), OrderLineModel.get(row[0])))
        return orders

    @classmethod
    def find_all(cls):
        """returns all orders placed by customers from the database
        
        Returns:
            list: all orders
        """
        conn = sqlite3.connect('db/webshop.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM orders ORDER BY id DESC')
        rows = cur.fetchall()
        conn.close()
        orders = list()
        for row in rows:
            user = UserModel.find(row[4])
            orders.append(OrderModel(row[0], row[1], row[2], row[3], user.json(), OrderLineModel.get(row[0])))
        return orders

    @classmethod
    def patch(cls, req_data, id):
        """changes order status and/or payment status in database for order with ID <id> and returns a message corresponding to the status
        
        Returns:
            dict: message corresponding to status
        """
        shippingStatus = "shipped"
        paymentStatus = "paid"
        if shippingStatus in req_data:
            status = req_data[shippingStatus]
            conn = sqlite3.connect('db/webshop.db')
            cur = conn.cursor()
            cur.execute("UPDATE orders SET " + shippingStatus + "=? WHERE id=" + str(id),
                        (int(status),))
            conn.commit()
            conn.close()
            return {'message': 'Verzendstatus successvol gewijzigd!'}
        if paymentStatus in req_data:
            status = req_data[paymentStatus]
            conn = sqlite3.connect('db/webshop.db')
            cur = conn.cursor()
            cur.execute("UPDATE orders SET " + paymentStatus + "=? WHERE id=" + str(id),
                        (int(status),))
            conn.commit()
            conn.close()
            return {'message': 'Betaingsstatus successvol gewijzigd!'}

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__