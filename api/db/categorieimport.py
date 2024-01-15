import sqlite3
import csv
conn = sqlite3.connect('shop/api/db/webshop.db')
cur = conn.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
categorieen (category_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL
        ) """

cur.execute(command1)
print("klantentabel aangemaakt")

fname=input('put csv file name: ')
if len(fname) < 1 : fname= "categorieen.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ';')
    for row in csv_reader:
        print(row)
        category_ID=row[0]
        category_name=row[1]
        cur.execute('''INSERT INTO categorieen(category_ID, category_name)
            VALUES (?,?)''',(category_ID, category_name))
        
conn.commit()
conn.close()