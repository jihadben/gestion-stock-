from django.urls import path
from . import views

# path('') : Cela spécifie l'URL qui déclenchera la vue. Dans cet exemple, l'URL est une chaîne vide '', ce qui signifie que cette vue sera associée à la racine du site. Lorsque l'utilisateur accède à la racine du site, la vue Add sera invoquée.

# views.Add : Cela spécifie la vue associée à l'URL. Dans Django, une vue est une fonction qui gère une requête HTTP particulière et renvoie une réponse. views.Add fait référence à la fonction Add dans le module views de votre application Django.

# name='Add' : Cela attribue un nom à l'URL. Le nom est utilisé pour référencer cette URL dans d'autres parties du code, généralement dans les modèles, les vues ou les fichiers de gabarits. Dans cet exemple, l'URL est nommée 'Add'.


urlpatterns =[
    # path('',views.product,name='product'),
     path('',views.Add,name='fournisseur'),
     path('delete/<int:pk>',views.delete,name='delete'),
     path('edit/<int:pk>',views.edit,name='edit'),

   
    ]