import sqlite3
import csv
conn = sqlite3.connect('shop/api/db/webshop.db')
cur = conn.cursor()

print("producttabel aangemaakt")

fname=input('csv file name: ')
if len(fname) < 1 : fname= "producten.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ';')
    for row in csv_reader:
        print(row)
        artikelnummer = row[0]
        artikelnaam = row[1]
        beschrijving = row[2]
        prijs = row[3]
        categorie = row[4]
        voorraad = row[5]
      
        cur.execute('''INSERT INTO products(code,title,description,price,category,stock)
            VALUES (?,?,?,?,?,?)''',(artikelnummer,artikelnaam,beschrijving,prijs,categorie,voorraad))
        
conn.commit()
conn.close()