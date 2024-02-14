from django import forms
from .models import Fournisseur

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

class FourForm(forms.ModelForm):
      class Meta:
        model = Fournisseur
        fields = ['Nom_Fournisseur' ,'Contact_Nom' ,'Contact_Telephone','Adresse', 'Ville','Code_Postal','Pays','Email','Site_Web']
        # widgets={
        #     'Nom_Fournisseur': forms.TextInput(attrs={'class':'form-control'}),
        #     'Contact_Nom': forms.TextInput(attrs={'class':'form-control'}),
        #     'Contact_Telephone': forms.NumberInput(attrs={'class':'form-control'}),
        #     'Adresse': forms.NumberInput(attrs={'class':'form-control'}),
        #     'Ville': forms.DateInput(attrs={'class':'form-control'}),

        #     }
