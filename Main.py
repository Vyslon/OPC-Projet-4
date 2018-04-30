# -*- coding: UTF-8 -*-
import requests
import json
from collections import deque

url_categories = "https://fr.openfoodfacts.org/categories.json"
r_categories = requests.get(url_categories).json()

categorie_list = []

products = deque()

for a in range(0, 20):
    categorie_list.append(r_categories['tags'][a]['url'])

print(categorie_list)

for k in range(0, 20):
    url_cat = categorie_list[k] + "/"
    for j in range(1, 21):
        final_url = url_cat + str(j) + ".json"
        r_products = requests.get(final_url).json()
        for i in range(0, 20):
            try:
                print("url : {}\n".format(final_url))
                print("{}\n".format(i))
                products.append({'nom' : r_products['products'][i]['product_name'],\
                'description' : r_products['products'][i]['categories'],\
                'revendeur(s)' : r_products['products'][i]['stores'],\
                'lien openfoodfacts' : r_products['products'][i]['url']})
            except:
                pass
print("Products : \n{}".format(products))

#nouvelle boucle pas encore commit, il faut trouver comment changer de page

#ajouter note nutritionnelle, categories des produits

#changer 20 pour une variable

#deque : fast appends and pop
