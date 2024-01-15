import sqlite3
import os
from flask import request
from models.category import CategoryModel
import re

class ProductModel:

    def __init__(self, id, code, title, description, price, category, stock, price_vat):
        """ProductModel constructor

        Args:
            id (int): database id
            code (string): product-code
            title (string): 
            description (string): 
            price (int): in cents
            category (int): category id 
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
    def find_all(cls, id):
        """returns all products with category id <id> in the database

        Returns:
            list: all products of chosen category
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE category=" + str(id) + " ORDER BY title", list())
        rows = cur.fetchall()
        conn.close()
        producten = list()
        for row in rows:
            vat = (row[4] * 1.21)
            producten.append(ProductModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], vat))

        return producten

    @classmethod
    def AllProducts(cls):
        """returns all products in the database

        Returns:
            list: all products
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM products ORDER BY title", list())
        rows = cur.fetchall()
        conn.close()
        producten = list()
        for row in rows:
            vat = (row[4] * 1.21)
            producten.append(ProductModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], vat))

        return producten

    @classmethod
    def FindProduct(cls, searchTerm):
        """returns all products with <searchterm> in the name or description in the database

        Returns:
            list: all products containing <searchterm> in name or description
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE title LIKE :var OR description LIKE :var", {'var': "%"+searchTerm+"%"})
        rows = cur.fetchall()
        conn.close()
        producten = list()
        for row in rows:
            vat = (row[4] * 1.21)
            producten.append(ProductModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], vat))

        return producten

    @classmethod
    def RegisterProduct(cls, req_data):
        """adds a product to the database if checks are in order and returns a message corresponding to the status

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
        requiredFields = [category, code, description, price, stock, title]
        for i in range(len(requiredFields)):
            if requiredFields[i] == "":
                return {'message': 'Alle verplichte velden (alle velden behalve price_vat) moeten ingevuld zijn!'} 
        categories = {}
        categoryModel = CategoryModel.find_all()
        categoriesList = [category.json() for category in categoryModel]
        for i in range(len(categoriesList)):
            categories[categoriesList[i]['name']] = categoriesList[i]['id']
        if category not in categories:
            return {'message': 'Ingevoerde categorie bestaat niet! (Let op, categorienaam is hoofdlettergevoelig)'}, 500
        if len(re.findall(regexCijfers, price)) != len(price):
            return {'message': 'Prijs moet een cijfer zijn!'}, 500
        if len(re.findall(regexCijfers, stock)) != len(stock):
            return {'message': 'Voorraad moet een cijfer zijn!'}, 500
        else:
            conn = sqlite3.connect("db/webshop.db")
            cur = conn.cursor()
            cur.execute('''INSERT INTO products(code, title, description, price, category, stock)
            VALUES (?,?,?,?,?,?)''',(code, title, description, int(price), int(categories[category]), int(stock)))
            conn.commit()
            conn.close()
            return {'message': 'Product is correct opgeslagen!'}, 200

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__