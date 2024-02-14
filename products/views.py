from django.shortcuts import render ,redirect 
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.
def product(request):
    produit = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST) #les donnees remplie par user est sont transmis par post dans cette variable form
        if form.is_valid():
            form.save()
            return redirect('product')
            
    else:
        form = ProductForm()

    context = {
        'pro': produit,
        'form': form,
    }
    
    return render(request, 'products/product.html', context)



def delete(request , pk):
   element=Product.objects.get(id=pk)
   
   if request.method =='POST':
      element.delete()
      
      return redirect('product')

    
   return render(request, 'products/delete.html') 


def edit(request , pk):
   element=Product.objects.get(id=pk)
   if request.method == 'POST':
     form=ProductForm(request.POST,instance=element)
     if form.is_valid():
        element.save()
        return redirect('product') 

   else :
      form=ProductForm(instance=element)
  
   context={
       'form':form
       }

   
   return render(request, 'products/edit.html',context)