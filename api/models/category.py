import sqlite3
import os

class CategoryModel:

    def __init__(self, id, name):
        """CategoryModel constructor

        Args:
            id (int): database id
            name (string): display name
        """
        self.id = id
        self.name = name

    @classmethod
    def find_all(cls):
        """returns all categories in the database and orders them by name

        Returns:
            list: all categories
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories ORDER BY name", list())
        rows = cur.fetchall()
        conn.close()
        categories = list()
        for row in rows:
            categories.append(CategoryModel(row[0], row[1]))
        return categories

    @classmethod
    def post(cls, req_data):
        """adds a category to the database and returns a message corresponding to the status

        Returns:
            dict: message corresponding to status
        """
        name = req_data['name']
        minimumCategoryNameLength = 3
        if len(name) < minimumCategoryNameLength:
            return {'message': 'Een categorienaam moet uit minimaal 3 karakters bestaan!'}, 500
        else:
            conn = sqlite3.connect("db/webshop.db")
            cur = conn.cursor()
            cur.execute('INSERT INTO categories(name) VALUES (?)',(name,))
            conn.commit()
            conn.close()
            return {'message': 'Categorie successvol toegevoegd!'}, 200

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__