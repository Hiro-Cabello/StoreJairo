from django.http import HttpResponse
from django.shortcuts import render

# ()   { }
#Recordar que luego de crear la funcion se tiene que asociar con una URL
#def index(request):
#    return HttpResponse('Hola Mundo!')


def index(request):
    return HttpResponse('Hola Mundo!')


#Renderizar
def examplerender(request):
    context = {
        'nombre': 'StoreJairo',
        'title' : 'Listado de Productos',
        'mensaje': 'Nuevo mensaje desde la vista',
        'products': [
           {'title':'Playera','price':5,'stock':True},
           {'title':'Camisa','price':7,'stock':True}, 
           {'title':'Mochila','price':20,'stock':False}, 
        ]
    }
    #la funcion render recibe 3 argumentos
    return render(request ,'index.html',context)








