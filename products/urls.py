from django.urls import path 
from . import views

urlpatterns = [
    #Con esto evitamos exponer el ID de los objetos al usuario final
    path('<slug:slug>',views.ProductDetailView.as_view(),name='product') # id --> llave primaria
]

