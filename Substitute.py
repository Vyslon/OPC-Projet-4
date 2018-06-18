import os
import records
import requests

nb_result = "0"
substitutes_id_list = []
categorie_list_name_S = []
restart = "0"

while (restart == "0"):
    nb_result = input("1 - Souhaitez-vous remplacer un aliment ?\n2 - "
                      "Retrouver mes aliments substitués.\n3 - Créer (1ère "
                      "utilisation) ou recréer (mise à jour) la base de "
                      "données\n\n")

    if nb_result == "1":
        url_categories = "https://fr.openfoodfacts.org/categories.json"
        r_categories = requests.get(url_categories).json()
        for a in range(0, 20):
            categorie_list_name_S.append(r_categories['tags'][a]['id'])
        db_connection = records.Database("mysql+pymysql://root:123@localhost/"
                                         "?charset=utf8mb4")
        db_connection.query("USE PROJET5;")
        name_product = input("Quel aliment Souhaitez-vous remplacer ?\n")
        rows = db_connection.query(
            "SELECT id FROM Products WHERE name = '{}';".format(name_product))
        id_product = rows.first()
        id_product = id_product["id"]
        rows_cat = db_connection.query("SELECT cat_id FROM"
                                       " PC_C_association_table WHERE "
                                       "product_id = {};".format(id_product))
        rc_list = []
        for el in rows_cat:
            rc_list.append(el.cat_id)
        rows_final = db_connection.query("SELECT Nom_Produit, "
                                         "Note_Nutritionnelle, Revendeurs, "
                                         "URL_off FROM VM_Final WHERE"
                                         " Nom_Categorie IN (\"{}\", \"{}\","
                                         "\"{}\") ORDER BY"
                                         " Note_Nutritionnelle;"
                                         .format(
                                            categorie_list_name_S[(
                                                rc_list[0]-1)],
                                            categorie_list_name_S[(
                                                rc_list[1]-1)],
                                            categorie_list_name_S[(
                                                rc_list[2]-1)]))
        substitute = rows_final[0]
        print("Nom du produit substitutant = {}\nNote nutritionnelle du "
              "produit substituant = {}\nRevendeur du produit substituant ="
              "{}\nlien openfoodfacts du produit substituant = {}\n\n"
              .format(
                  substitute["Nom_Produit"], substitute["Note_Nutritionnelle"],
                  substitute["Revendeurs"], substitute["URL_off"]))
        save = input("Voulez vous sauvegarder le produit substitutant ? 1 -"
                     " Sauvegarder 2 - Ne pas sauvegarder\n")
        if save == "1":
            rows_substitute = db_connection.query("SELECT id FROM Products "
                                                  "WHERE name = \"{}\""
                                                  .format(
                                                      substitute[
                                                          "Nom_Produit"]))
            id_substitute = rows_substitute.first()
            id_substitute = id_substitute["id"]
            db_connection.query("UPDATE Products SET substitute = true WHERE "
                                "id = \"{}\"".format(id_substitute))
            print("Produit substituant sauvegardé")
        restart = input("0 - Retour menu\n1 - Fermer programme\n\n")
    elif nb_result == "2":
        db_connection = records.Database("mysql+pymysql://root:123@localhost/"
                                         "?charset=utf8mb4")
        db_connection.query("USE PROJET5;")
        substitutes = db_connection.query("SELECT name, url_openfoodfact FROM"
                                          " Products WHERE substitute = true;")
        print("Liste des produits substituants : \n======================\n\n")
        for x in substitutes:
            print("Nom produit substituant : {}\nURL Open Food Facts produit"
                  " substituant : {}\n\n".format(x.name, x.url_openfoodfact))
        restart = input("0 - Retour menu\n1 - Fermer programme\n\n")
    elif nb_result == "3":
        os.system("python3 /home/thomas/Openclassrooms/Projet_5/OPC-Projet-4/"
                  "Create_database.py")
        restart = input("0 - Retour menu\n1 - Fermer programme\n\n")
