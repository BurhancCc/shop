-- Creator:       MySQL Workbench 8.0.22/ExportSQLite Plugin 0.1.0
-- Author:        burha
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2021-01-04 18:49
-- Created:       2021-01-02 15:10
PRAGMA foreign_keys = OFF;

-- Schema: mydb
ATTACH "webshop.db" AS "mydb";
BEGIN;
CREATE TABLE "mydb"."Categorieen"(
  "category_name" VARCHAR(45) PRIMARY KEY NOT NULL
);
INSERT INTO "Categorieen"("category_name") VALUES('Boxsprings');
INSERT INTO "Categorieen"("category_name") VALUES('Bedden');
INSERT INTO "Categorieen"("category_name") VALUES('Bedbodems');
INSERT INTO "Categorieen"("category_name") VALUES('Beddengoed');
INSERT INTO "Categorieen"("category_name") VALUES('Matrassen');
INSERT INTO "Categorieen"("category_name") VALUES('Kussens');
INSERT INTO "Categorieen"("category_name") VALUES('Kasten');
CREATE TABLE "mydb"."Klanten"(
  "customer_email" VARCHAR(45) PRIMARY KEY NOT NULL,
  "customer_name" VARCHAR(45) NOT NULL,
  "customer_surname_prefix" VARCHAR(45),
  "customer_surname" VARCHAR(45) NOT NULL,
  "customer_street" VARCHAR(45) NOT NULL,
  "customer_house_number" INTEGER NOT NULL,
  "customer_address_suffix" VARCHAR(45),
  "customer_postal_code" VARCHAR(45) NOT NULL,
  "customer_city" VARCHAR(45) NOT NULL,
  "customer_country" VARCHAR(45) NOT NULL,
  "customer_password" VARCHAR(45) NOT NULL,
  "customer_newsletter_status" INTEGER NOT NULL
);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('cindi.wellings@fake.windesheim.nl', 'Cindi', '', 'Wellings', 'Cardinal', 7085, '', '7514 AB', 'Enschede', 'Netherlands', '89LrhcTr', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('rebekkah.chanson@fake.windesheim.nl', 'Rebekkah', 'le', 'Chanson', 'Kerkstraat', 3, '', '1354 CD', 'Almere Haven', 'Netherlands', 'mszbAQuw', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('shelli.baumert@fake.windesheim.nl', 'Shelli', '', 'Baumert', 'Forest Run', 3, '', '6224 ED', 'Maastricht', 'Netherlands', '73GxLtAj', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('ayn.jollye@fake.windesheim.nl', 'Ayn', '', 'Jollye', 'Superior', 25, 'b', '7514 AG', 'Enschede', 'Netherlands', 'pux8DHQc', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('rodrigo.kobelt@fake.windesheim.nl', 'Rodrigo', '', 'Kobelt', 'Bashford', 673, '', '1170 GH', 'Bruxelles', 'Belgium', '55KvETMn', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('glenden.tellenbroker@fake.windesheim.nl', 'Glenden', '', 'Tellenbroker', 'Reinke', 0, '', '7536 AS', 'Tournai', 'Belgium', 'tJKp5njS', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('bellanca.kenshole@fake.windesheim.nl', 'Bellanca', '', 'Kenshole', 'Arrowood', 25, '', '4874 CC', 'Etten-Leur', 'Netherlands', 'bLfPRAxW', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('lexine.follows@fake.windesheim.nl', 'Lexine', '', 'Follows', 'Fremont', 2, '', '1209 EA', 'Hilversum', 'Netherlands', 'HfJTecTv', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('rachael.harroway@fake.windesheim.nl', 'Rachael', '', 'Harroway', 'Birchwood', 891, '', '6042 KB', 'Charleroi', 'Belgium', 'f85z83Bf', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('gavra.beeson@fake.windesheim.nl', 'Gavra', '', 'Beeson', 'Iowa', 83, '', '3009 DF', 'Rotterdam postbusnummers', 'Netherlands', 'zNKaW3mk', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('robinson.baude@fake.windesheim.nl', 'Robinson', '', 'Baude', 'Shopko', 34, '', '8229 AS', 'Lelystad', 'Netherlands', '6BqfFzKh', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('marcile.coats@fake.windesheim.nl', 'Marcile', '', 'Coats', 'Blue Bill Park', 89, '', '2334 HA', 'Leiden', 'Netherlands', 'SUDeJAmu', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('merrili.hassard@fake.windesheim.nl', 'Merrili', '', 'Hassard', 'Chive', 2796, '', '2019 EA', 'Haarlem', 'Netherlands', '6kb7FYTT', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('huntington.antonomoli@fake.windesheim.nl', 'Huntington', '', 'Antonomoli', 'Independence', 5, '', '3104 BB', 'Schiedam', 'Netherlands', 'PmmAYu86', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('annemarie.ducaen@fake.windesheim.nl', 'Annemarie', '', 'Ducaen', 'Lukken', 557, '', '5914 DA', 'Venlo', 'Netherlands', 'vxcu3pQJ', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('frederigo.kellard@fake.windesheim.nl', 'Frederigo', '', 'Kellard', 'Nelson', 6, '2h', '6709 FE', 'Wageningen', 'Netherlands', '3gwMKJDN', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('keefer.stygall@fake.windesheim.nl', 'Keefer', '', 'Stygall', 'Stygall', 5, '', '9674 CB', 'Winschoten', 'Netherlands', 'Q4cXy6AN', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('amandi.megarrell@fake.windesheim.nl', 'Amandi', '', 'Megarrell', 'Summerview', 38, '', '2624 DD', 'Delft', 'Netherlands', 'VvjQKhtP', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('shane.duffett@fake.windesheim.nl', 'Shane', '', 'Duffett', 'Bultman', 4, '', '7004 AC', 'Doetinchem', 'Netherlands', 'xrgPBCAe', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('gifford.lindstedt@fake.windesheim.nl', 'Gifford', 'van', 'Lindstedt', 'Roth', 292, '', '3324 CH', 'Dordrecht', 'Netherlands', 'mwbqNyfc', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('kipper.soares@fake.windesheim.nl', 'Kipper', '', 'Soares', 'Oakridge', 1, 'hs', '7554 AL', 'Hengelo', 'Netherlands', 'FUjQhQN5', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('tillie.skeen@fake.windesheim.nl', 'Tillie', '', 'Skeen', 'Old Shore', 2, '', '6464 FA', 'Kerkrade', 'Netherlands', 'dtKzSHvY', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('drugi.wear@fake.windesheim.nl', 'Drugi', '', 'Wear', 'Northfield', 3, '', '5914 AJ', 'Venlo', 'Netherlands', 'JyTcYc6X', 1);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('gherardo.sorton@fake.windesheim.nl', 'Gherardo', '', 'Sorton', 'Corry', 119, '', '9730 DB', 'Groningen', 'Netherlands', 'TKBgnrd8', 0);
INSERT INTO "Klanten"("customer_email","customer_name","customer_surname_prefix","customer_surname","customer_street","customer_house_number","customer_address_suffix","customer_postal_code","customer_city","customer_country","customer_password","customer_newsletter_status") VALUES('ozzy.bonnick@fake.windesheim.nl', 'Ozzy', 'de', 'Bonnick', 'Del Mar', 1, '', '2170 SA', 'Antwerpen', 'Belgium', 'AURcnThz', 1);
CREATE TABLE "mydb"."Producten"(
  "product_model_number" VARCHAR(45) PRIMARY KEY NOT NULL,
  "product_name" VARCHAR(45) NOT NULL,
  "product_category" VARCHAR(45) NOT NULL,
  "product_description" VARCHAR(45) NOT NULL,
  "product_price_in_cents_before_VAT" INTEGER NOT NULL,
  "product_supplier" VARCHAR(45) NOT NULL,
  "date_added" DATE NOT NULL,
  "current_stock" INTEGER NOT NULL,
  CONSTRAINT "productcategorie"
    FOREIGN KEY("product_category")
    REFERENCES "Categorieen"("category_name")
);
CREATE INDEX "mydb"."Producten.productcategorie_idx" ON "Producten" ("product_category");
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BS-0123987', 'Boxspring Jumpy-01', 'Boxsprings', 'Het meest veerkrachtige bed van Nederland', 149900, 'Beddenmeester bv', '2020/01/01', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BS-0123555', 'Boxspring Jumpy-02', 'Boxsprings', 'Het een-na-meest veerkrachtige bed van Nederland', 139900, 'Beddenmeester bv', '2020/01/01', 23);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BSL-2332', 'Boxspring Lelystad', 'Boxsprings', 'Een fantastische boxspring', 99900, 'BestBed', '2020/05/03', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BSZ-2322', 'Boxspring Zeewolde', 'Boxsprings', 'Een weergaloze boxspring', 85400, 'Beddenfabriek', '2020/04/02', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BSA-3444', 'Boxspring Almere-Buiten', 'Boxsprings', 'Misschien wel de beste boxspring van Nederland', 190000, 'Beddenfabriek', '2020/03/01', 6);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BSU-1122', 'Boxspring Urk', 'Boxsprings', 'Een prachtige boxspring', 150000, 'BestBed', '2020/02/02', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-001', 'Standaard eenpersoonsbed', 'Bedden', 'Bed voor 1 persoon (90 cm)', 23300, 'BestBed', '2020/03/04', 20);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-002', 'Standaard tweepersoonsbed', 'Bedbodems', 'Bed voor 2 personen (180 cm)', 49900, 'BestBed', '2020/03/04', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('W-12', 'Wollen deken', 'Beddengoed', 'Een deken van echt schapenwol', 25900, 'Schapenwol United', '2020/04/01', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('DB-12', '4-seizoenendekbed', 'Beddengoed', 'Een winter- en zomerdeel van 100% katoen', 12000, 'Beddenmeester bv', '2020/06/04', 19);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('MBV-01', 'Binnenveringsmatras', 'Matrassen', 'De goede ventilatie is het grote voordeel van een binnenveringsmatras', 25999, 'Matrassengroothandel Snurk bv', '2020/05/02', 31);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('KS-023', 'Kussen Softy', 'Kussens', 'Kussen gevuld met eendendons', 4995, 'De Kussengigant bv', '2020/04/23', 12);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('KS-035', 'Kussen Hard', 'Kussens', 'Kussen gevuld met knikkers', 3595, 'De Kussengigant bv', '2020/05/06', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('KS-028', 'Kussen Firm', 'Kussens', 'Kussen gevuld met kamelenhaar', 2495, 'De Kussengigant bv', '2020/05/06', 16);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('MB-02', 'Matrasbeschermer Solid', 'Matrassen', 'Matrasbeschermer extra stevig', 6995, 'BestBed', '2020/04/12', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('DB-13', 'Dekbedovertrek Sunny Flowers', 'Beddengoed', 'Dekbed overtrek met zonnebloemen design', 4495, 'Xanderella ', '2020/08/03', 8);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('DB-16', 'Dekbedovertrek Uni Blauw', 'Beddengoed', 'Dekbedovertrek uni kleur donkerblauw', 2995, 'Xanderella ', '2020/08/04', 7);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('MH-003', 'Molton Matrashoes Select', 'Beddengoed', 'Molton matrashoes om je matras te beschermen', 3250, 'Beddenmeester bv', '2020/03/23', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('MH-011', 'Molton Matrashoes Superior', 'Beddengoed', 'Molton matrashoes extra dik om je matras te beschermen', 4295, 'Beddenmeester bv', '2020/03/23', 5);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-06', 'Lattenbodem BiFlex 300', 'Bedbodems', 'Solide lattenbodem van beukenhout met extra veerkracht', 8995, 'BestBed', '2020/09/12', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-08', 'Lattenbodem BiFlex 400', 'Bedbodems', 'Solide lattenbodem van beukenhout met extra brede latten', 7995, 'BestBed', '2020/09/12', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-11', 'Lattenbodem Electra 2000', 'Bedbodems', 'Elektrisch verstelbare lattenbodem', 15500, 'BestBed', '2020/07/11', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-13', 'Lattenbodem Electra 2000Z', 'Bedbodems', 'Elektrisch verstelbare lattenbodem op zonneenergie', 18500, 'BestBed', '2020/07/13', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-22', 'Lattenbodem DiscFlex 500', 'Bedbodems', 'Solide schotelbodem vlak', 19950, 'BestBed', '2020/05/08', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('LB-24', 'Lattenbodem DiscFlex 500E', 'Bedbodems', 'Solide schotelbodem volledig elektrisch verstelbaar', 25500, 'BestBed', '2020/05/08', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('ML-09', 'Latex matras Gold de luxe', 'Matrassen', 'Stevige latex matras van natuurlatex 1 persoon (90 cm)', 79900, 'Matrassengroothandel Snurk bv', '2020/04/03', 5);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('ML-06', 'Latex matras Silver', 'Matrassen', 'Stevige latex matras van synth. latex (90 cm)', 33900, 'Matrassengroothandel Snurk bv', '2020/04/03', 7);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('ML-03', 'Matras Candy Original', 'Matrassen', 'Koudschuimmatras 1 persoons (90 cm) hardheid medium', 22500, 'Matrassengroothandel Snurk bv', '2020/04/06', 6);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('ML-02', 'Matras Sliver Foam ', 'Matrassen', 'Koudschuimmatras 1 persoons (80 cm) hardheid stevig', 19950, 'Matrassengroothandel Snurk bv', '2020/04/06', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-009', 'Stapelbed Huub', 'Bedden', 'Wit stapelbed voor kinderen tot 8 jaar', 35500, 'Beddenfabriek', '2020/02/03', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-012', 'Twijfelaar Kweetniet', 'Bedden', 'Twijfelaar 120 cm breed met stalen buizenframe', 22500, 'Beddenfabriek', '2020/02/04', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-013', 'Hoogslaper Empire State', 'Bedden', 'Hoogslaper met bureau ', 37500, 'Beddenfabriek', '1950/02/05', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BB-007', 'Babybed Pamper', 'Bedden', 'Voor de kleine slaper', 19900, 'beddenfabriek', '2020/03/12', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('OLB-003', 'Seniorenbed Krakkemikkig', 'Bedden', 'Seniorenbed met hoge instap en valhekjes 1 persoons (90 cm)', 41500, 'beddenfabriek', '2020/07/10', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('OLB-004', 'Seniorenbed Kist', 'Bedden', 'Seniorenbed extra smal (50 cm) van eikenfineer voorzien van handvaten om het makkelijk te kunnen verplaatsen', 89900, 'Kistenmaker bv', '2020/07/13', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SLB-002', 'Slaapbank Amro', 'Bedden', 'Slaapbank te vergroten van 1 naar 2 persoons', 62500, 'Beddenmeester bv', '2020/01/09', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('VB-004', 'Vouwbed Origami', 'Bedden', 'Vouwbed met wieltjes (80 cm) kan op meerdere manieren opgevouwen worden', 9900, 'BestBed', '2020/02/23', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('OKB-001', 'Opklapbed Pats Boem', 'Bedden', 'Opklapbed met witte multiplex ombouw (90 cm)', 22500, 'BestBed', '2020/07/07', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-007', 'Hoogslaper Moonraker', 'Bedden', 'Hoogslaper met bureau + (schiet)stoel', 57500, 'James Bedden bv', '2020/02/02', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('DB-007', 'Dekbedovertrek Octopussy', 'Beddengoed', 'Dekbedovertrek met afbeeldingen van zeevissen', 6250, 'James Bedden bv', '2020/02/02', 5);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('ED-002', 'Elektrische deken Shock', 'Beddengoed', 'Elektrische deken voor de koude wintermaanden  1 persoons (80 cm)', 3500, 'Beddenmeester bv', '2020/10/12', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SB-150', 'Twijfelaar Corona', 'Bedden', 'Extra brede twijfelaar van 150 cm', 27500, 'Beddenfabriek', '2020/03/13', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('BS-007', 'Boxspring Q', 'Boxsprings', 'Super innovatieve boxspring, bij het herkennen van snurkgeluiden schiet het hoofdeinde automatisch omhoog' , 139900, 'James Bedden bv', '2020/09/12', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('KS-011', 'Kussen Polly', 'Beddengoed', 'Kussen met een schapenwollen vulling speciaal bedoeld voor personen met een pollen allergie', 7995, 'Xanderella ', '2020/06/19', 4);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('DB-03', 'Dekbed Vivaldi', 'Beddengoed', '4 seizoenen dekbed met schapenwollen vulling ', 9495, 'Beddenmeester bv', '2020/06/06', 5);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('NK-02', 'Nachtkastje Rembrandt', 'Kasten', 'Mooi gelakt en gepolieteerd nachtkastje van kersenhout ', 39500, 'Nachtwacht bv', '2020/10/11', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('NK-03', 'Commode Varaan', 'Kasten', 'Commode met 5 laden, maakt je slaapkamer helmaal compleet', 29900, 'Nachtwacht bv', '2020/10/11', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SK-04', 'Schuifdeurkast Easy', 'Kasten', 'Prachtige schuifdeurkast met 2 deuren 160cm breed', 47500, 'Nachtwacht bv', '2020/10/13', 1);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SK-06', 'Schuifdeurkast Rough', 'Kasten', 'Mooie stevige schuifdeur kast 3 deuren waarvan 1 met spiegel', 67500, 'Nachtwacht bv', '2020/10/13', 2);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('SK-02', 'Draaideurkast Crimineel', 'Kasten', 'Simpele maar solide draaideurkast met 2 deuren ', 31500, 'Nachtwacht bv', '2020/10/14', 3);
INSERT INTO "Producten"("product_model_number","product_name","product_category","product_description","product_price_in_cents_before_VAT","product_supplier","date_added","current_stock") VALUES('HB-01', 'Boxspring Attila', 'Boxsprings', 'Oerdegelijk hunnebed van speciaal geselecteerde gladgeslepen Zweedse keien ', 142500, 'Beddenmeester bv', '2020/11/01', 2);
COMMIT;