DROP DATABASE IF EXISTS PROJ5;
CREATE DATABASE PROJ5;

GRANT ALL PRIVILEGES ON mydb.* TO 'vyn'@'localhost' WITH GRANT OPTION;

USE PROJ5;

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
  id INT UNSIGNED AUTO_INCREMENT NOT NULL,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(200),
  stores VARCHAR(100),
  nutrition_grade CHAR(1) NOT NULL,
  substituting_product_id INT UNSIGNED,
  PRIMARY KEY(id)
)ENGINE = InnoDB;

ALTER TABLE Products
ADD CONSTRAINT fk_sub_prod_id FOREIGN KEY Products(substituting_product_id) REFERENCES Products(id);

DROP TABLE IF EXISTS PC_C_association_table;
CREATE TABLE PC_C_association_table (
    product_id INT UNSIGNED NOT NULL,
    cat_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (product_id, cat_id)
)ENGINE = InnoDB;

ALTER TABLE PC_C_association_table
ADD CONSTRAINT fk_cat_id FOREIGN KEY PC_C_association_table(product_id) REFERENCES Products(id);

ALTER TABLE PC_C_association_table
ADD CONSTRAINT fk_product_id FOREIGN KEY PC_C_association_table(cat_id) REFERENCES Products_categories(id);

CREATE INDEX ind_nutrition_grade
ON Products(nutrition_grade);

CREATE INDEX ind_product_id
ON PC_C_association_table(product_id);

CREATE INDEX ind_cat_id
ON PC_C_association_table(cat_id);

DROP TABLE IF EXISTS Products_categories;
CREATE TABLE Products_categories (
  id INT UNSIGNED AUTO_INCREMENT NOT NULL,
  name VARCHAR(200) NOT NULL,
  PRIMARY KEY(id)
)ENGINE = InnoDB;

CREATE UNIQUE INDEX unique_name
ON Products_categories(name);

DROP TABLE IF EXISTS VM_Final;
CREATE TABLE VM_Final
ENGINE = InnoDB
SELECT Products.name AS Nom_Produit, Products.nutrition_grade AS Note_Nutritionnelle, Products.description AS Description, Products.stores AS Revendeurs, Products_categories.name AS Nom_Catégorie
FROM PC_C_association_table
INNER JOIN Products_categories ON PC_C_association_table.cat_id = Products_categories.id
INNER JOIN Products ON PC_C_association_table.product_id = Products.id
ORDER BY Products.nutrition_grade
