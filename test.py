import records

db_connection = records.Database('mysql+pymysql://root:123@localhost')
db_connection.query("DROP DATABASE IF EXISTS PROJET5;")
db_connection.query("CREATE DATABASE PROJET5;")
db_connection.query("USE PROJET5;")
db_connection.query("DROP TABLE IF EXISTS Products;")
db_connection.query("CREATE TABLE Products (id INT UNSIGNED AUTO_INCREMENT NOT NULL, name VARCHAR(100) NOT NULL, description VARCHAR(200), stores VARCHAR(100), nutrition_grade CHAR(1) NOT NULL, substituting_product_id INT UNSIGNED, PRIMARY KEY(id))")
db_connection.query("ALTER TABLE Products ADD CONSTRAINT fk_sub_prod_id FOREIGN KEY Products(substituting_product_id) REFERENCES Products(id);")
db_connection.query("DROP TABLE IF EXISTS PC_C_association_table;")
db_connection.query("CREATE TABLE PC_C_association_table (product_id INT UNSIGNED NOT NULL, cat_id INT UNSIGNED NOT NULL, PRIMARY KEY (product_id, cat_id))ENGINE = InnoDB;")
db_connection.query("CREATE INDEX ind_nutrition_grade ON Products(nutrition_grade);")
db_connection.query("CREATE INDEX ind_product_id ON PC_C_association_table(product_id);")
db_connection.query("CREATE INDEX ind_cat_id ON PC_C_association_table(cat_id);")
db_connection.query("DROP TABLE IF EXISTS Products_categories;")
db_connection.query("CREATE TABLE Products_categories (id INT UNSIGNED AUTO_INCREMENT NOT NULL, name VARCHAR(200) NOT NULL, PRIMARY KEY(id))ENGINE = InnoDB;")
db_connection.query("ALTER TABLE PC_C_association_table ADD CONSTRAINT fk_cat_id FOREIGN KEY PC_C_association_table(product_id) REFERENCES Products(id);")
db_connection.query("ALTER TABLE PC_C_association_table ADD CONSTRAINT fk_product_id FOREIGN KEY PC_C_association_table(cat_id) REFERENCES Products_categories(id);")
db_connection.query("CREATE UNIQUE INDEX unique_name ON Products_categories(name);")
db_connection.query("DROP TABLE IF EXISTS VM_Final;")
db_connection.query("CREATE TABLE VM_Final ENGINE = InnoDB SELECT Products.name AS Nom_Produit, Products.nutrition_grade AS Note_Nutritionnelle, Products.description AS Description, Products.stores AS Revendeurs, Products_categories.name AS Nom_Catégorie FROM PC_C_association_table INNER JOIN Products_categories ON PC_C_association_table.cat_id = Products_categories.id INNER JOIN Products ON PC_C_association_table.product_id = Products.id ORDER BY Products.nutrition_grade;")

"{}".format(var) POUR REMPLIR LA BASE DE DONNEES
