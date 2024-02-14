from django.db import models
from fournisseurs.models import Fournisseur

# Create your models here.

class Product(models.Model):
    nom_produit=models.CharField(max_length=100 )
    ID_Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE , default=1)
    description=models.CharField(max_length=100)
    prix_unitaire=models.FloatField(max_length=200)
    quantite_en_stock=models.CharField(max_length=100)
    date_creation=models.DateField(max_length=100,)
    
class Meta :
    db_table="stockgestion.produits_produits"  