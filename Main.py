# -*- coding: UTF-8 -*-
import requests
import json

url = "https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux.json/get?page=2"
r = requests.get(url).json()

dictionnary = {"pbfabP1" : [],
"pbfabP2" : [],
"pbfabP3" : [],
"pbfabP4" : [],
"pbfabP5" : [],
"pbfabP6" : [],
"pbfabP7" : [],
"pbfabP8" : [],
"pbfabP9" : [],
"pbfabP10" : [],
"pbfabP11" : [],
"pbfabP12" : [],
"pbfabP13" : [],
"pbfabP14" : [],
"pbfabP15" : [],
"pbfabP16" : [],
"pbfabP17" : [],
"pbfabP18" : [],
"pbfabP19" : [],
"pbfabP20" : [],
}
for j in range(1, 20):
    dic_name = "pbfabP" + str(j)
    for i in range(20):
        dictionnary[dic_name].append({'nom' : r['products'][i]['product_name_fr']})
        dictionnary[dic_name].append({'description' : r['products'][i]['categories']})
        dictionnary[dic_name].append({'revendeur(s)' : r['products'][i]['stores']})
        dictionnary[dic_name].append({'lien openfoodfacts' : r['products'][i]['url']})
print("pbfabP1 : \n{}".format(dictionnary["pbfabP1"]))

#nouvelle boucle pas encore commit, il faut trouver comment changer de page
