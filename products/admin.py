from django.contrib import admin

#Importamos el modelo
from .models import Product

#registramos el modelo()

class ProductoAdmin(admin.ModelAdmin):
    fields=('title','description','price','image')
    list_display = ('__str__','slug','created_at')
    #search_fields=('title')

admin.site.register(Product,ProductoAdmin)

