import sqlite3
import os
import json
from models.userrole import UserroleModel
from models.country import CountryModel
from models.order_line import OrderLineModel
from flask import request
from flask_restful import Resource
import re
from flask_jwt import JWT, jwt_required, current_identity

class UserModel:

    def __init__(self, id, email, password, firstname, infix, lastname, street, housenumber, zipcode, city, newsletter, userrole, country):
        """UserModel constructor

        Args:
            id (int): database id
            email (string): 
            password (string): 
            firstname (string): 
            infix (string): can be emtpy
            lastname (string): 
            street (string): 
            housenumber (int):
            zipcode (string): 
            city (string): 
            newsletter (int): 1 for yes, 0 for no
            userrole (int): userrole id
            country (int): country id
        """
        self.id = id
        self.email = email
        self.password = password
        self.firstname = firstname
        self.infix = infix
        self.lastname = lastname
        self.street = street
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.city = city
        self.newsletter = newsletter
        self.userrole = userrole
        self.country = country

    @classmethod
    def find(cls, id):
        """returns single user ID'd <id> from the database

        Returns:
            list: single user
        """
        conn = sqlite3.connect("db/webshop.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=" + str(id), list())
        user_row = cur.fetchone()
        conn.close()
        user = list()
        user.append(UserModel(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], user_row[6], user_row[7], user_row[8], user_row[9], user_row[10], user_row[11], user_row[12]))
        # return the requested user
        return user[0]

    @classmethod
    def Register(cls, req_data):
        """registers a user to the database according to <req_data> after performing checks and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        regex = "[a-zA-Z]"
        regexKlein = "[a-z]"
        regexGroot= "[A-Z]"
        regexCijfers = "[0-9]"
        regexMetSpaties = "[a-zA-Z ]"
        regexEmail = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        firstname = req_data['firstname']
        infix = req_data['infix']
        lastname = req_data['lastname']
        street = req_data['street']
        housenumber = req_data['housenumber']
        zipcode = req_data['zipcode']
        city = req_data['city']
        country = req_data['country']
        email = req_data['email']
        password = req_data['password']
        newsletter = req_data['newsletter']
        userrole = 1

        landIDs = {'Netherlands': '1', 'Belgium': '2'}

        verplichteKlantGegevens = [firstname, lastname, street, housenumber, zipcode, city, country, email, password, newsletter]
        for i in range(len(verplichteKlantGegevens)):
           if verplichteKlantGegevens[i] == None or verplichteKlantGegevens[i] == "":
                return {'message': 'Alle verplichte velden (alle velden behalve tussenvoegsel) moeten ingevuld zijn!'}
        if len(re.findall(regexCijfers, housenumber)) != len(housenumber):
            return {'message': 'Een huisnummer mag alleen uit cijfers bestaan!'}
        if country == landIDs['Netherlands']:
            verbodenNlPostcodeEindes = ['sa', 'sd', 'ss', 'SA', 'SD', 'SS', 'Sa', 'Sd', 'Ss', 'sA', 'sD', 'sS']
            if len(zipcode) != 6:
                return {'message': 'Een Nederlandse postcode moet uit 6 karakters bestaan en formaat 1234AB hebben!'}
            if zipcode[0] == '0':
                return {'message': 'Een Nederlandse postcode kan niet met een 0 beginnen!'}
            if zipcode[4] + zipcode[5] in verbodenNlPostcodeEindes:
                return {'message': 'Een Nederlandse postcode kan niet met \'SA\', \'SD\' of \'SS\' eindigen!'}
            for i in range(len(zipcode)):
                if i >= 1 and i <= 3:
                    if re.findall(regexCijfers, zipcode[i]) == []:
                        return {'message': 'Een Nederlandse postcode moet formaat 1234AB hebben!'}
                if i > 3:
                    if re.findall(regex, zipcode[i]) == []:
                        return {'message': 'Een Nederlandse postcode moet formaat 1234AB hebben!'}
        if country == landIDs['Belgium']:
            postcodeSinterklaasBelgie = "0612"
            if len(zipcode) != 4:
                return {'message': 'Een Belgische postcode moet uit 4 cijfers bestaan!'}
            for i in range(len(zipcode)):
                if re.findall(regexCijfers, zipcode[i]) == []:
                    return {'message': 'Een Belgische postcode moet uit 4 cijfers bestaan!'}
            if zipcode == postcodeSinterklaasBelgie:
                return {'message': 'Mooi geprobeerd, maar Sinterklaas woont in Spanje!'}
            if int(zipcode) < 1000:
                return {'message': 'Een Belgische postcode moet van 1000 t/m 9999 gaan!'}
        if country not in landIDs.values():
            if len(re.findall(regexCijfers, zipcode)) != len(zipcode):
                return {'message': 'Een poscode mag alleen uit cijfers bestaan!'}

        minimumEmailLengte = 5
        if len(email) < minimumEmailLengte:
            return {'message': 'Een emailadres moet minimaal 5 karakters lang zijn!'}
        if not re.search(regexEmail, email):  
            return {'message': 'Een emailadres moet formaat mail@host.com hebben!'}
        
        minimumWachtwoordLengte = 8
        if (re.findall(regexKlein, password) == [] or re.findall(regexCijfers, password) == []
            or re.findall(regexGroot, password) == [] or len(password) < minimumWachtwoordLengte):
            return{'message': 'Een wachtwoord moet minimaal 8 karakters lang zijn, waarvan minimaal een hoofdletter, een kleine letter en 1 cijfer!'}
        
        else:
            conn = sqlite3.connect('db/webshop.db')
            cur = conn.cursor()
            cur.execute('''INSERT INTO users(email, password, firstname, infix, lastname, street, housenumber, zipcode, city, newsletter, userrole_id, country_id)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',(email, password, firstname, infix, lastname, street, housenumber, zipcode, city, int(newsletter), userrole, int(country)))
            conn.commit()
            conn.close()
            return {'message': 'Registratie successvol!'}, 200

    @classmethod
    def login(cls, email, password):
        """ Deze functie kijkt welke gebruiker hoort bij het ingevoerde email en password.
        als de ingevoerde gegevens kloppen dan returnt hij het goed, zoniet geeftie niks terug.
        Deze functie geeft mee email en password 
        Args:
        path (path): path to requested file

        Returns:
        string: file content
        """

        con = sqlite3.connect("db/webshop.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?",(email, password))
        user_row = cur.fetchone()
        if user_row:
            user = UserModel(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], user_row[6], user_row[7], user_row[8], user_row[9], user_row[10], user_row[11], user_row[12])
            return user

    @classmethod
    def patch(cls, req_data, id):
        """updates user ID'd <id> in the database according to <req_data> after performing checks and returns a message corresponding to the status

        Returns:
            dict: a message corresponding to status
        """
        regex = "[a-zA-Z]"
        regexKlein = "[a-z]"
        regexGroot= "[A-Z]"
        regexCijfers = "[0-9]"
        regexMetSpaties = "[a-zA-Z ]"
        regexEmail = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        firstname = req_data['firstname']
        infix = req_data['infix']
        lastname = req_data['lastname']
        street = req_data['street']
        housenumber = req_data['housenumber']
        zipcode = req_data['zipcode']
        city = req_data['city']
        country = req_data['country']
        email = req_data['email']
        newsletter = req_data['newsletter']

        landIDs = {'Netherlands': '1', 'Belgium': '2'}

        verplichteKlantGegevens = [firstname, lastname, street, housenumber, zipcode, city, country, email, newsletter]
        for i in range(len(verplichteKlantGegevens)):
           if verplichteKlantGegevens[i] == None or verplichteKlantGegevens[i] == "":
                return {'message': 'Alle verplichte velden (alle velden behalve tussenvoegsel) moeten ingevuld zijn!'}, 500
        if len(re.findall(regexCijfers, housenumber)) != len(housenumber):
            return {'message': 'Een huisnummer mag alleen uit cijfers bestaan!'}, 500
        if country == landIDs['Netherlands']:
            verbodenNlPostcodeEindes = ['sa', 'sd', 'ss', 'SA', 'SD', 'SS', 'Sa', 'Sd', 'Ss', 'sA', 'sD', 'sS']
            if len(zipcode) != 6:
                return {'message': 'Een Nederlandse postcode moet uit 6 karakters bestaan en formaat 1234AB hebben!'}, 500
            if zipcode[0] == '0':
                return {'message': 'Een Nederlandse postcode kan niet met een 0 beginnen!'}
            if zipcode[4] + zipcode[5] in verbodenNlPostcodeEindes:
                return {'message': 'Een Nederlandse postcode kan niet met \'SA\', \'SD\' of \'SS\' eindigen!'}, 500
            for i in range(len(zipcode)):
                if i >= 1 and i <= 3:
                    if re.findall(regexCijfers, zipcode[i]) == []:
                        return {'message': 'Een Nederlandse postcode moet formaat 1234AB hebben!'}, 500
                if i > 3:
                    if re.findall(regex, zipcode[i]) == []:
                        return {'message': 'Een Nederlandse postcode moet formaat 1234AB hebben!'}, 500
        if country == landIDs['Belgium']:
            postcodeSinterklaasBelgie = "0612"
            if len(zipcode) != 4:
                return {'message': 'Een Belgische postcode moet uit 4 cijfers bestaan!'}, 500
            for i in range(len(zipcode)):
                if re.findall(regexCijfers, zipcode[i]) == []:
                    return {'message': 'Een Belgische postcode moet uit 4 cijfers bestaan!'}, 500
            if zipcode == postcodeSinterklaasBelgie:
                return {'message': 'Mooi geprobeerd, maar Sinterklaas woont in Spanje!'}, 500
            if int(zipcode) < 1000:
                return {'message': 'Een Belgische postcode moet van 1000 t/m 9999 gaan!'}, 500
        if country not in landIDs.values():
            if len(re.findall(regexCijfers, zipcode)) != len(zipcode):
                return {'message': 'Een poscode mag alleen uit cijfers bestaan!'}, 500

        minimumEmailLengte = 5
        if len(email) < minimumEmailLengte:
            return {'message': 'Een emailadres moet minimaal 5 karakters lang zijn!'}, 500
        if not re.search(regexEmail, email):
            return {'message': 'Een emailadres moet formaat mail@host.com hebben!'}, 500
        else:
            conn = sqlite3.connect('db/webshop.db')
            cur = conn.cursor()
            cur.execute("UPDATE users SET email=?, firstname=?, infix=?, lastname=?, street=?, housenumber=?, zipcode=?, city=?, newsletter=?, country_id=? WHERE id=" + str(id),
                        (email, firstname, infix, lastname, street, int(housenumber), zipcode, city, int(newsletter), int(country)))
            conn.commit()
            conn.close()
            return {'message': 'Registratie successvol!'}, 200

    def json(self):
        """Returns a JSON version of the current object


        """
        self_dict = self.__dict__

        userrole = UserroleModel.find(self.userrole)
        self_dict["userrole"] = userrole.json()

        country = CountryModel.find(self.country)
        self_dict["country"] = country.json()

        return self_dict
