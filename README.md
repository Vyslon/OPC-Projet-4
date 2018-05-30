# [EN] Healthier

**Healthier is an application which will allow you to clean up your food habits by finding substitutes to your favorite products !**
 
 - [ ] To begin, 2 options are available to you, you can start the creation of the database of the application by launching  "**Create_database.py**" script or you can make it by launching "**Substitute.py**", by entering `3` in the terminal
 




> Create_database.py has to be already executed to use the application properly. (to find substitutes)
>
>Create_database.py is sending HTTP requests to [Open Food Facts](https://fr.openfoodfacts.org) which is an open source  database of food products.


 - [ ] To find a substitute for the food that you want, you have to launch Substitute.py (once the database have been created) then input `1` in the terminal and finally input the name (in French) of the food for which you want a substitute
 

>Every Open Food Facts's food is not available in the application in order to have a correct execution time, but you can fix this by changing the value of the `nb_of_categories` variable


 - [ ] You can find all your substituting food by entering 2 in the terminal, after launching Substitute.py

# [FR] Healthier

**Healthier est une application qui vous permettra d'assainir vos habitudes alimentaires en trouvant des substituts à vos produits préférés !**

 - [ ] Pour commencer, 2 options s'offrent à vous, vous pouvez lancer la
       création de la base de données de l'application en lançant le
       script "**Create_database.py**" ou vous pouvez le faire en
       lançant le script "**Substitute.py**" (Tappez 3 dans le terminal)

> Create_database.py devra donc être exécuter pour utiliser le programme, que ce soit en lançant le script directement ou alors en demandant la création de la base de données via Substitute.py.
> 
> Create_database.py envoie des requêtes HTTP au site [Open Food Facts](https://fr.openfoodfacts.org) qui est une banque de données de produits alimentaires open source.

 - [ ] Pour trouver un substitut à l'aliment que vous souhaitez, vous devez lancer Substitute.py (et avoir lancer la création de la base de données, regardez plus haut dans la documentation si vous ne l'avez pas encore fait), tapper 1 et entrer dans la console le nom (en français), de l'aliment pour lequel vous souhaitez trouver un substitut 
 
 

> Tout les aliments d'Open Food Facts ne sont pas disponibles dans l'application, mais vous pouvez arranger ça en remplaçant la valeur de la variable `nb_of_categories` par le nombre de catégories présentes dans Open Food Facts

 - [ ] Vous pouvez retrouver vos aliments substituants en tappant 2 dans le terminal, lorsque vous avez lancer Substitute.py
