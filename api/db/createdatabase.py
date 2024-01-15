import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
sql_file = open("shop/api/db/Database.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)
