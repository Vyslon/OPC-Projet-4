# OPC-Projet-4

**Healthier is an application which will allow you to clean up your food habits by finding substitutes to your favorite products !**
 
 - [ ] To begin, 2 options are available to you, you can start the creation of the database of the application by launching  "**Create_database.py**" script or you can make it by launching "**Substitute.py**", by entering `3` in the terminal

> Create_database.py has to be already executed to use the application properly. (to find substitutes)
>
>Create_database.py is sending HTTP requests to [Open Food Facts](https://fr.openfoodfacts.org) which is an open source  database of food products.

 - [ ] To find a substitute for the food that you want, you have to launch Substitute.py (once the database have been created) then input `1` in the terminal and finally input the name (in French) of the food for which you want a substitute

>Every Open Food Facts's food is not available in the application in order to have a correct execution time, but you can fix this by changing the value of the `nb_of_categories` variable

 - [ ] You can find all your substituting food by entering 2 in the terminal, after launching Substitute.py
