import sqlite3
import os
import json


class UserroleModel:

    def __init__(self, id, name):
        """UserroleModel constructor

        Args:
            id (int): database id
            name (string): display name of the userrole
        """
        self.id = id
        self.name = name

    @classmethod
    def find_all(cls):
        """returns all userroles in the database

        Returns:
            list: all userroles
        """
        userroles = list()
        con = sqlite3.connect("db/webshop.db")

        cur = con.cursor()

        for userrole in cur.execute('SELECT id, name FROM userroles'):
            userrole_1 = UserroleModel(userrole[0], userrole[1])
            userroles.append(userrole_1)
        return userroles

    @classmethod
    def find(cls, userrole_id):
        """returns userrole ID'd <userrole_id> in the database

        Returns:
            list: single userrole
        """
        con = sqlite3.connect("db/webshop.db")

        cur = con.cursor()
        cur.execute('SELECT * FROM userroles WHERE id=?', [userrole_id])
        userrole_row = cur.fetchone()
        userrole = UserroleModel(userrole_row[0], userrole_row[1])
        return userrole

    def json(self):
        """Returns a JSON version of the current object


        """
        self_dict = self.__dict__

        return self_dict