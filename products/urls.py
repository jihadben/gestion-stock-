from django.urls import path
from . import views

urlpatterns =[
    path('',views.product,name='product'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
   
    ]