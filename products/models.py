from django.db import models


from django.utils.text import slugify
#callback es una funcion que se pasa a otra funcion como argumento

from django.db.models.signals import pre_save

# Create your models here.
#Los atributos de esta clase va ser las columnas de las tablas

class Product(models.Model):
    title = models.CharField(max_length=50) 
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8 , decimal_places=2 , default=0.0) #12345678.98
    slug = models.SlugField(null=False,blank=False , unique=True)
    created_at = models.DateTimeField(auto_now_add=True) # Este valor se toma de forma automatica cuando el registro se inserte

    #Vamos a sobreescribir métofo save  *args arcgumentos y **kwargs diccionario de argumentos       
    #def save(self,*args,**kwargs):
    #    self.slug = slugify(self.title)
    #    super(Product , self).save(*args , **kwargs)


    #Signal o señales se usa para notificar ciertas acciones que suceden
    #dentro de la aplicacion 

    #Esto es para poder ver el admin el nombre del title
    def __str__(self):
        return self.title
    

def set_slug(sender , instance , *args , **kwargs):#callback
    instance.slug = slugify(instance.title)

pre_save.connect(set_slug , sender =Product )



