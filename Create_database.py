# -*- coding: UTF-8 -*-
import requests
import json
import records
from collections import deque
from functions import *

url_categories = "https://fr.openfoodfacts.org/categories.json"
r_categories = requests.get(url_categories).json()
categorie_list_url = []
categorie_list_name = []
categorie_list_id = []
products = deque()
nb_categories_produits = 20

db_connection = records.Database('mysql+pymysql://root:123@localhost')
db_connection.query("SET NAMES 'utf8';")
db_connection.query("SET CHARACTER SET utf8;")
db_connection.query("DROP DATABASE IF EXISTS PROJET5;")
db_connection.query("CREATE DATABASE PROJET5 CHARACTER SET utf8 COLLATE utf8_general_ci;;")
db_connection.query("USE PROJET5;")
db_connection.query("DROP TABLE IF EXISTS Products;")
db_connection.query("CREATE TABLE Products (id INT UNSIGNED AUTO_INCREMENT NOT NULL, name VARCHAR(100) NOT NULL, description VARCHAR(200), stores VARCHAR(100), nutrition_grade CHAR(1) NOT NULL, substitued_by_product_id INT UNSIGNED, url_openfoodfact VARCHAR(100) NOT NULL, PRIMARY KEY(id))")
db_connection.query("ALTER TABLE Products ADD CONSTRAINT fk_sub_prod_id FOREIGN KEY Products(substitued_by_product_id) REFERENCES Products(id);")
db_connection.query("DROP TABLE IF EXISTS PC_C_association_table;")
db_connection.query("CREATE TABLE PC_C_association_table (product_id INT UNSIGNED NOT NULL, cat_id INT UNSIGNED NOT NULL, PRIMARY KEY (product_id, cat_id))ENGINE = InnoDB;")
db_connection.query("CREATE INDEX ind_nutrition_grade ON Products(nutrition_grade);")
db_connection.query("CREATE INDEX ind_product_id ON PC_C_association_table(product_id);")
db_connection.query("CREATE INDEX ind_cat_id ON PC_C_association_table(cat_id);")
db_connection.query("DROP TABLE IF EXISTS Products_categories;")
db_connection.query("CREATE TABLE Products_categories (id INT UNSIGNED AUTO_INCREMENT NOT NULL, name VARCHAR(200) NOT NULL, PRIMARY KEY(id))ENGINE = InnoDB;")
db_connection.query("ALTER TABLE PC_C_association_table ADD CONSTRAINT fk_cat_id FOREIGN KEY PC_C_association_table(product_id) REFERENCES Products(id);")
db_connection.query("ALTER TABLE PC_C_association_table ADD CONSTRAINT fk_product_id FOREIGN KEY PC_C_association_table(cat_id) REFERENCES Products_categories(id);")
db_connection.query("CREATE UNIQUE INDEX unique_name ON Products_categories(name);")
db_connection.query("DROP TABLE IF EXISTS VM_Final;")
db_connection.query("CREATE TABLE VM_Final ENGINE = InnoDB SELECT Products.name AS Nom_Produit, Products.nutrition_grade AS Note_Nutritionnelle, Products.description AS Description, Products.stores AS Revendeurs, Products_categories.name AS Nom_Categorie, url_openfoodfact AS URL_off  FROM PC_C_association_table INNER JOIN Products_categories ON PC_C_association_table.cat_id = Products_categories.id INNER JOIN Products ON PC_C_association_table.product_id = Products.id ORDER BY Products.nutrition_grade;")
db_connection.query("ALTER TABLE Products CONVERT TO CHARACTER SET utf8;")
db_connection.query("ALTER TABLE PC_C_association_table CONVERT TO CHARACTER SET utf8;")
db_connection.query("ALTER TABLE Products_categories CONVERT TO CHARACTER SET utf8;")
db_connection.query("ALTER TABLE VM_Final CONVERT TO CHARACTER SET utf8;")


for a in range(0, nb_categories_produits):
    categorie_list_url.append(r_categories['tags'][a]['url'])
    categorie_list_name.append(r_categories['tags'][a]['name'])
    categorie_list_id.append(r_categories['tags'][a]['id'])

for nb in range(0, nb_categories_produits):
    db_connection.query("INSERT INTO Products_categories (name) VALUES (\"{}\");".format(categorie_list_name[nb]))

for k in range(0, nb_categories_produits):
    url_cat = categorie_list_url[k] + "/"
    for j in range(1, 21):
        final_url = url_cat + str(j) + ".json"
        r_products = requests.get(final_url).json()
        for i in range(0, nb_categories_produits):
            try:
                products.append({'nom' : r_products['products'][i]['product_name'],\
                'description' : r_products['products'][i]['categories'],\
                'revendeur(s)' : r_products['products'][i]['stores'],\
                'lien openfoodfacts' : r_products['products'][i]['url'],\
                'note nutritionnelle' : r_products['products'][i]['nutrition_grade_fr'],\
                'cat0' : r_products['products'][i]['categories_hierarchy'][0],\
                'cat1' : r_products['products'][i]['categories_hierarchy'][1],\
                'cat2' : r_products['products'][i]['categories_hierarchy'][2],
                })
            except:
                pass
