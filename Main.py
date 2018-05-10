# -*- coding: UTF-8 -*-
import requests
import json
import pymysql.cursors
from collections import deque
from functions import *

url_categories = "https://fr.openfoodfacts.org/categories.json"
r_categories = requests.get(url_categories).json()
categorie_list_url = []
categorie_list_name = []
products = deque()
nb_categories_produits = 20
db_connection = pymysql.connect(host='localhost',
                                user='root',
                                password='123',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

try:
    with db_connection.cursor() as cur:
        sql = "SOURCE /home/thomas/Openclassrooms/Projet_5/OPC-Projet-4/database.SQL"
        cur.execute(sql)

    db_connection.commit()

    with db_connection.cursor() as cur:
        sql = "SHOW TABLES;"
        cur.execute(sql)
        result = cur.fetchnone()
        print(result)
except:
    pass
finally:
    db_connection.close()

for a in range(0, nb_categories_produits):
    categorie_list_url.append(r_categories['tags'][a]['url'])

for a in range(0, nb_categories_produits):
    categorie_list_name.append(r_categories['tags'][a]['name'])

for k in range(0, nb_categories_produits):
    url_cat = categorie_list_url[k] + "/"
    for j in range(1, 21):
        final_url = url_cat + str(j) + ".json"
        r_products = requests.get(final_url).json()
        for i in range(0, nb_categories_produits):
            try:
                #print("url : {}\n".format(final_url))
                #print("{}\n".format(i))
                products.append({'nom' : r_products['products'][i]['product_name'],\
                'description' : r_products['products'][i]['categories'],\
                'revendeur(s)' : r_products['products'][i]['stores'],\
                'lien openfoodfacts' : r_products['products'][i]['url'],\
                'note nutritionnelle' : r_products['products'][i]['nutrition_grade_fr'],\
                'cat0' : r_products['products'][i]['categories_hierarchy'][0],\
                'cat1' : r_products['products'][i]['categories_hierarchy'][1],\
                'cat2' : r_products['products'][i]['categories_hierarchy'][2],
                })
                #print(r_products['products'][i]['stores'])
            except:
                pass
