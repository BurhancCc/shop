import sqlite3
import csv
conn = sqlite3.connect('shop/api/db/webshop.db')
cur = conn.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
users (klantid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        voornaam TEXT NOT NULL,
        tussenvoegsel TEXT NULL,
        achternaam TEXT NOT NULL,
        straat TEXT NOT NULL,
        huisnummer INT NOT NULL,
        postcode TEXT NOT NULL,
        woonplaats TEXT NOT NULL,
        land INT NOT NULL,
        email TEXT NOT NULL,
        wachtwoord TEXT NOT NULL,
        nieuwsbrief INT NOT NULL,
        CONSTRAINT "landID"
            FOREIGN KEY ("land")
            REFERENCES "landen"("country_ID")
        ) """

cur.execute(command1)
print("klantentabel aangemaakt")

fname=input('put csv file name: ')
if len(fname) < 1 : fname= "klanten.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ';')
    for row in csv_reader:
        print(row)
        voornaam=row[0]
        tussenvoegsel=row[1]
        achternaam=row[2]
        straat=row[3]
        huisnummer=row[4]
        postcode =row[5]
        woonplaats=row[6]
        land=row[7]
        email=row[8]
        wachtwoord=row[9]
        nieuwsbrief=row[10]
        cur.execute('''INSERT INTO users(voornaam, tussenvoegsel, achternaam, straat, huisnummer, postcode, woonplaats, land, email, wachtwoord, nieuwsbrief)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(voornaam, tussenvoegsel, achternaam, straat, huisnummer, postcode, woonplaats, land, email, wachtwoord, nieuwsbrief))
        
conn.commit()
conn.close()