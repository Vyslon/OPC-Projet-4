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
nb_of_categories = 20
p_id = 0

db_connection = records.Database(
    "mysql+pymysql://root:123@localhost"
    "/?charset=utf8mb4")
db_connection.query("SET NAMES 'UTF8MB4';")
db_connection.query("SET CHARACTER SET UTF8MB4;")
db_connection.query("DROP DATABASE IF EXISTS PROJET5;")
db_connection.query("CREATE DATABASE PROJET5;")
db_connection.query(
    "ALTER DATABASE PROJET5 CHARACTER SET UTF8MB4 "
    "COLLATE utf8mb4_general_ci;")
db_connection.query("USE PROJET5;")
db_connection.query("DROP TABLE IF EXISTS Products;")
db_connection.query(
    "CREATE TABLE Products (id INT UNSIGNED AUTO_INCREMENT"
    " NOT NULL, name VARCHAR(100) NOT NULL, description VARCHAR(200), "
    "stores VARCHAR(100), nutrition_grade CHAR(1) NOT NULL, substitute "
    "BOOLEAN, url_openfoodfact VARCHAR(100) NOT NULL,"
    " PRIMARY KEY(id))ENGINE = InnoDB;")
db_connection.query("DROP TABLE IF EXISTS PC_C_association_table;")
db_connection.query(
    "CREATE TABLE PC_C_association_table (product_id INT "
    "UNSIGNED, cat_id INT UNSIGNED, PRIMARY KEY (product_id, cat_id))"
    "ENGINE = InnoDB;")
db_connection.query(
    "CREATE INDEX ind_nutrition_grade ON "
    "Products(nutrition_grade);")
db_connection.query(
    "CREATE INDEX ind_product_id ON "
    "PC_C_association_table(product_id);")
db_connection.query(
    "CREATE INDEX ind_cat_id ON "
    "PC_C_association_table(cat_id);")
db_connection.query("DROP TABLE IF EXISTS Products_categories;")
db_connection.query(
    "CREATE TABLE Products_categories (id INT UNSIGNED "
    "AUTO_INCREMENT NOT NULL, name VARCHAR(200) NOT NULL, PRIMARY KEY(id))"
    "ENGINE = InnoDB;")
db_connection.query(
    "CREATE UNIQUE INDEX unique_cat_name ON "
    "Products_categories(name);")
db_connection.query("CREATE UNIQUE INDEX unique_name ON Products(name);")
db_connection.query("DROP TABLE IF EXISTS VM_Final;")
db_connection.query("ALTER TABLE Products CONVERT TO CHARACTER SET UTF8MB4;")
db_connection.query(
    "ALTER TABLE PC_C_association_table CONVERT TO CHARACTER SET "
    "UTF8MB4;")
db_connection.query(
    "ALTER TABLE Products_categories CONVERT TO CHARACTER SET "
    "UTF8MB4;")


for a in range(0, nb_of_categories):
    categorie_list_url.append(r_categories['tags'][a]['url'])
    categorie_list_name.append(r_categories['tags'][a]['id'])
    print(r_categories['tags'][a]['id'])

for nb in range(0, nb_of_categories):
    cdc = "INSERT INTO Products_categories (name) VALUES (\"{}\");"
    db_connection.query(cdc.format(categorie_list_name[nb]))

for k in range(0, nb_of_categories):
    url_cat = categorie_list_url[k] + "/"
    for j in range(1, 21):
        final_url = url_cat + str(j) + ".json"
        r_products = requests.get(final_url).json()
        for i in range(0, nb_of_categories):
            try:
                insertion_prod = 0
                prod_name = r_products['products'][i]['product_name']
                prod_description = r_products['products'][i]['categories']
                prod_stores = r_products['products'][i]['stores']
                prod_nutrinion_grade = \
                r_products['products'][i]['nutrition_grades_tags'][0]
                prod_url_openfoodfact = r_products['products'][i]['url']
                prod_categorie_1 = \
                r_products['products']\
                [i]['categories_hierarchy'][0]
                prod_categorie_2 = \
                r_products['products']\
                [i]['categories_hierarchy'][1]
                prod_categorie_3 = \
                r_products['products']\
                [i]['categories_hierarchy'][2]
                pc_id_1 = cat_into_cat_id(prod_categorie_1,
                 categorie_list_name)
                pc_id_2 = cat_into_cat_id(prod_categorie_2,
                 categorie_list_name)
                pc_id_3 = cat_into_cat_id(prod_categorie_3,
                 categorie_list_name)
                if (len(prod_name) <= 100 and len(prod_description) <= 200 and
                    len(prod_stores) <= 100 and len(prod_nutrinion_grade) == 1 and
                    len(prod_url_openfoodfact) <= 100 and pc_id_1 != 100 and
                    pc_id_2 != 100 and pc_id_3 != 100):
                    insertion_prod = db_connection.query("INSERT INTO Products (name, description, stores, nutrition_grade, url_openfoodfact) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\");".format(prod_name, prod_description, prod_stores, prod_nutrinion_grade, prod_url_openfoodfact))
            except:
                pass
            try:
                 if insertion_prod != 0:
                    p_id = p_id + 1
                    insertion_association_1 = \
                    "INSERT INTO PC_C_association_table" \
                    " (product_id, cat_id) VALUES ({}, {})" \
                    ";"
                    insertion_association_2 = \
                    "INSERT INTO PC_C_association_table" \
                    " (product_id, cat_id) VALUES ({}, {})" \
                    ";"
                    insertion_association_3 = \
                    "INSERT INTO PC_C_association_table" \
                    " (product_id, cat_id) VALUES ({}, {})" \
                    ";"
                    db_connection.query(insertion_association_1.format(p_id, pc_id_1))
                    db_connection.query(insertion_association_2.format(p_id, pc_id_2))
                    db_connection.query(insertion_association_3.format(p_id, pc_id_3))
            except:
                pass

db_connection.query(
    "CREATE TABLE VM_Final ENGINE = InnoDB SELECT "
    "Products.name AS Nom_Produit, Products.nutrition_grade AS "
    "Note_Nutritionnelle, Products.description AS Description, "
    "Products.stores AS Revendeurs, Products_categories.name AS"
    " Nom_Categorie, url_openfoodfact AS URL_off  FROM PC_C_association_table"
    " INNER JOIN Products_categories ON PC_C_association_table.cat_id = "
    "Products_categories.id INNER JOIN Products ON "
    "PC_C_association_table.product_id = Products.id ORDER BY "
    "Products.nutrition_grade;")
db_connection.query("ALTER TABLE VM_Final CONVERT TO CHARACTER SET UTF8MB4;")
