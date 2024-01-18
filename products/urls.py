from django.urls import path 
from . import views

#Ahora las rutas pueden tener el mismo nombre  
#app_name='products'

urlpatterns = [
    path('search',views.ProductSearchListView.as_view() , name='search'),
    #Con esto evitamos exponer el ID de los objetos al usuario final
    path('<slug:slug>',views.ProductDetailView.as_view(),name='product') ,# id --> llave primaria
    
]

