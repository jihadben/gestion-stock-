from django.shortcuts import render,redirect
from .models import Fournisseur
from .forms import FourForm
# Create your views here.

def Add(request):
    Four = Fournisseur.objects.all()
    if request.method == 'POST':
      formule=FourForm(request.POST)
      if formule.is_valid():
         formule.save()
         return redirect('fournisseur')
    else :
      # Si la requête n'est pas une méthode POST, crée un formulaire FourForm vide
      formule=FourForm() 
           


    Data ={
        'getdata':Four,
        'formule':formule
        }
    return render(request,'fournisseurs/fournisseur.html',Data)


def delete(request,pk):
   
   if request.method == 'POST':
      data=Fournisseur.objects.get(id=pk)
      data.delete()
      return redirect('fournisseur')

   return render(request,'fournisseurs/delete.html') 


def edit(request , pk):
   element=Fournisseur.objects.get(id=pk)
   if request.method == 'POST':
     form=FourForm(request.POST,instance=element)
     if form.is_valid():
        element.save()
        return redirect('fournisseur') 

   else :
      form=FourForm(instance=element)
  
   context={
       'form':form
       }

   
   return render(request, 'fournisseurs/edit.html',context)