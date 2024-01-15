import sqlite3
import os

class CountryModel:

    def __init__(self, id, name):
        """CountryModel constructor

        Args:
            id (int): database id
            name (string): country name
        """
        self.id = id
        self.name = name

    @classmethod
    def find_all(cls):
        """returns all countries in the database

        Returns:
            list: all countries
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries ORDER BY name", list())
        rows = cur.fetchall()
        conn.close()
        countries = list()
        for row in rows:
            countries.append(CountryModel(row[0], row[1]))
        return countries

    @classmethod
    def find(cls, country_id):
        """returns a single with ID <country_id> country in the database

        Returns:
            list: single country
        """
        con = sqlite3.connect("db/webshop.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM countries WHERE id=?', [country_id])
        country_row = cur.fetchone()

        country = CountryModel(country_row[0], country_row[1])

        return country

    @classmethod
    def post(cls, req_data):
        """adds a country to the database and return a message corresponding to the status

        Returns:
            dict: message corresponding to status
        """
        name = req_data['name']
        minimumCountryNameLength = 4

        if len(name) < minimumCountryNameLength:
            return {'message': 'Een landnaam moet minimaal 4 letters zijn!'}, 500
        else:
            conn = sqlite3.connect("db/webshop.db")
            cur = conn.cursor()
            cur.execute('INSERT INTO countries(name) VALUES (?)',(name.title(),))
            conn.commit()
            conn.close()
            return {'message': 'Land successvol opgeslagen!'}

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__