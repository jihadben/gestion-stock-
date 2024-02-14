from django.db import models

# Create your models here.

# ID_Fournisseur INT PRIMARY KEY,
#     Nom_Fournisseur VARCHAR(50) NOT NULL,
#     Contact_Nom VARCHAR(50),
#     Contact_Telephone VARCHAR(15),
#     Adresse VARCHAR(100),
#     Ville VARCHAR(50),
#     Code_Postal VARCHAR(10),
#     Pays VARCHAR(50),
#     Email VARCHAR(50),
#     Site_Web VARCHAR(100) 
class Fournisseur(models.Model):
    Nom_Fournisseur=models.CharField(max_length=100 )
    Contact_Nom=models.CharField(max_length=100)
    Contact_Telephone=models.CharField(max_length=200)
    Adresse=models.CharField(max_length=100)
    Ville=models.CharField(max_length=100,)
    Code_Postal=models.CharField(max_length=100,)
    Pays=models.CharField(max_length=100,)
    Email=models.CharField(max_length=100,)
    Site_Web=models.CharField(max_length=100,)
class Meta :
    db_table="stockgestion.produits_produits"  


   