# -*- coding: UTF-8 -*-
import requests
import json

url = "https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux/3.json"
r = requests.get(url).json()

dictionnary = {"pbfabP" : []
}
for j in range(1, 20):
    dic_name = "pbfabP"
    for i in range(20):
        dictionnary[dic_name].append({'nom' : r['products'][i]['product_name_fr']})
        dictionnary[dic_name].append({'description' : r['products'][i]['categories']})
        dictionnary[dic_name].append({'revendeur(s)' : r['products'][i]['stores']})
        dictionnary[dic_name].append({'lien openfoodfacts' : r['products'][i]['url']})
print("pbfabP : \n{}".format(dictionnary["pbfabP"]))

#nouvelle boucle pas encore commit, il faut trouver comment changer de page
