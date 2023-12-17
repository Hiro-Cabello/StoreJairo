from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset  = Product.objects.all().order_by('-id')
    
    #vamos a sobreescribir el método
    #Con este método vamos a pasar el contexto de la clase al template
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs) #con esto obtenemos el contexto de la clase padre
        context['title'] = 'Listado de productos'
        context['products']= context['product_list']
        
        print(context)
        
        
        return context

#Vamos a generar un vista donde podamos conocer más a detalle el producto
#Recordar que la clase DetailView va buscar un objeto mediante un identificador unico
#Y el valor del identificador lo va tomar de la url
class ProductDetailView(DetailView): #id-->pk
    model = Product
    template_name = 'products/product.html'
    
    #def get_context_data(self , **kwargs):
    #    context = super().get_context_data(**kwargs) #con esto obtenemos el contexto de la clase padre 
    #    print(context)
    #    return context #con esto le estoy pasando los datos al template