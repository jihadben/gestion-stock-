from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nom_produit' ,'description' ,'prix_unitaire','quantite_en_stock', 'date_creation','ID_Fournisseur']
        widgets={
            'nom_produit': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Fournisseur': forms.NumberInput(attrs={'class':'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class':'form-control'}),
            'quantite_en_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'date_creation': forms.DateInput(attrs={'class':'form-control'}),
            
            }




