# Generated by Django 5.0.1 on 2024-02-07 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ID_Fournisseur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fournisseurs.fournisseur'),
        ),
    ]
