# -*- coding: UTF-8 -*-
import requests

r = requests.get("https://fr.openfoodfacts.org/categories.json")
print("reponse : {}".format(r.text))
