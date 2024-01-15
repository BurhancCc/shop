import sqlite3
import csv
conn = sqlite3.connect('shop/api/db/webshop.db')
cur = conn.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
landen (country_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        country_name TEXT NOT NULL
        ) """

cur.execute(command1)
print("landentabel aangemaakt")

fname=input('put csv file name: ')
if len(fname) < 1 : fname= "landen.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ';')
    for row in csv_reader:
        print(row)
        country_ID=row[0]
        country_name=row[1]
        cur.execute('''INSERT INTO landen(country_ID, country_name)
            VALUES (?,?)''',(country_ID, country_name))
        
conn.commit()
conn.close()