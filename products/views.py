from django.shortcuts import render
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


#Para poder realizar una consulta aplicando diversos filtros se tiene que importar lo siguiente
from django.db.models import Q

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




class ProductSearchListView(ListView):
   
    template_name = 'products/search.html'  
    # Plantilla que se usará para renderizar la lista de objetos
    # renderizar implica tomar datos y combinarlos con una plantilla
    # para producir un resultadoque se enviará la navegador web del usuario.
    
    #Las clases que hereden de detailview
    #Aqui vamos a depender de lo que el formulario nos envíe como input
    def get_queryset(self):
        #Aquí se puede identificar el filtro doble
        filters = Q(title__icontains = self.query()) | Q(category__title__icontains = self.query())
        #Select * from productos where title like %valor%
        #return Product.objects.filter(title__icontains = self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')
     
    #vamos a sobreescribir el método
    #Con este método vamos a pasar el contexto de la clase al template
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs) #con esto obtenemos el contexto de la clase padre
        context['query']= self.query()
        context['products']= self.get_queryset()
        context['count']=context['products'].count()
        print(context)
        return context