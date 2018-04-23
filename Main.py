# -*- coding: UTF-8 -*-
import requests
import json

url = "https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux.json"
r = requests.get(url).json()

dictionnary = {"pbfabP1" : []}
for i in range(20):
    dictionnary["pbfabP1"].append({'nom' : r['products'][i]['product_name_fr']})
    dictionnary["pbfabP1"].append({'description' : r['products'][i]['categories']})
    dictionnary["pbfabP1"].append({'revendeur(s)' : r['products'][i]['stores']})
    dictionnary["pbfabP1"].append({'lien openfoodfacts' : r['products'][i]['url']})
print("pbfabP1 : \n{}".format(dictionnary["pbfabP1"]))
