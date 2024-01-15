import sqlite3
import os
import re
from models.category import CategoryModel

class oneProductModel:

    def __init__(self, id, code, title, description, price, category, stock, price_vat):
        """ProductModel constructor

        Args:
            id (int): database id
            code (string): product-code
            title (string): 
            description (string): 
            price (int): in cents
            category (dict): dict containing category ID and category name
            stock (int): amount in stock
            price_vat (int): price in vat
        """
        self.id = id
        self.code = code
        self.title = title
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.price_vat = price_vat

    @classmethod
    def find(cls, id):
        """returns a single product with id <id> from the database

        Returns:
            list: a single product
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=" + str(id), list())
        row = cur.fetchall()
        conn.close()
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories WHERE id=" + str(row[0][5]), list())
        categoryRow = cur.fetchall()
        conn.close()
        category = {}
        category['id'] = categoryRow[0][0]
        category['name'] = categoryRow[0][1]
        product = list()
        vat = (row[0][4] * 1.21)
        product.append(oneProductModel(row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], category, row[0][6], vat))

        return product[0]

    @classmethod
    def patch(cls, req_data, id):
        """performs checks and if all correct edits product ID'd <id> in the database according to <req_data> and returns a message corresponding to status
        
        Returns:
            dict: message corresponding to status
        """
        regexCijfers = "[0-9]"
        category = req_data['category']
        code = req_data['code']
        description = req_data['description']
        price = req_data['price']
        price_vat = req_data['price_vat']
        stock = req_data['stock']
        title = req_data['title']
        categories = {}
        categoryModel = CategoryModel.find_all()
        requiredFields = [category, code, description, price, stock, title]
        for i in range(len(requiredFields)):
            if requiredFields[i] == "":
                return {'message': 'Alle verplichte velden (alle velden behalve price_vat) moeten ingevuld zijn!'} 
        categoriesList = [category.json() for category in categoryModel]
        for i in range(len(categoriesList)):
            categories[categoriesList[i]['id']] = categoriesList[i]['name']
        if len(re.findall(regexCijfers, price)) != len(price):
            return {'message': 'Prijs moet een cijfer zijn!'}, 500
        if len(re.findall(regexCijfers, stock)) != len(stock):
            return {'message': 'Voorraad moet een cijfer zijn!'}, 500
        else:
            conn = sqlite3.connect("db/webshop.db")
            cur = conn.cursor()
            cur.execute("UPDATE products SET code=?, title=?, description=?, price=?, category=?, stock=? WHERE id=" + str(id),
                        (code, title, description, int(price), int(category), int(stock)))
            conn.commit()
            conn.close()
            return {'message': 'Product is successvol gewijzigd!'}, 200

    @classmethod
    def delete(cls, id):
        """deletes a single product with id <id> from the database if it's not part of an unshipped/unpaid order and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM order_lines WHERE product=' + str(id))
        orderLines = cur.fetchall()
        orders = list()
        for i in range(len(orderLines)):
            cur.execute('SELECT * FROM orders WHERE id=' + str(orderLines[i][2]))
            orders.append(cur.fetchall())
        notPaidAndOrShippedStatus = 0
        for i in range(len(orders)):
            if orders[i][0][2] == notPaidAndOrShippedStatus or orders[i][0][3] == notPaidAndOrShippedStatus:
                return {'message': 'Product kan niet verwijderd worden omdat het nog onderdeel is van een lopende bestelling!'}, 500
        cur.execute('DELETE FROM products WHERE id=' + str(id))
        conn.commit()
        conn.close()
        return {'message': 'Product successvol verwijderd!'}, 200
    
    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
