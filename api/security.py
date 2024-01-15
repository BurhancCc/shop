import os
import sqlite3
from resources import *
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from flask_jwt import JWT, jwt_required, current_identity
import json
from models.userrole import UserroleModel

def authenticate(email, password):
    print("User successfully authenticated")
    user = UserModel.login(email, password)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    print("Something went wrong. Authentication doesn't work")


def identity(payload):
    print("User successfully identified")
    con = sqlite3.connect("db/webshop.db")
    cur = con.cursor()
    user_id = "%s" % payload['identity']
    for user_row in cur.execute("SELECT * FROM users WHERE id =" + user_id):
        user = UserModel(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], user_row[6], user_row[7], user_row[8], user_row[9], user_row[10], user_row[11], user_row[12])
        # print(json.dumps(user.dict, indent=4, sort_keys=True))
        return user
    print("Something went wrong. Identify doesn't work")