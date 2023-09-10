from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect

# ()   {}  <!--  -->
#Recordar que luego de crear la funcion se tiene que asociar con una URL
#def index(request):
#    return HttpResponse('Hola Mundo!')



#Nos permite autenticar a un usuario
from django.contrib.auth import authenticate

#Ahora vamos a usar esta funcion para poder crear la sesion
from django.contrib.auth import login

#Ahora vamos a usar esta funcion para poder cerrar la sesion
from django.contrib.auth import logout

#Para enviar mensajes del servidor al cliente
from django.contrib import messages

#def index(request):
#    return HttpResponse('Hola Mundo!')

def index(request):
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

def login_views(request):#Tiene que recibir la peticion
    #va responder con un template
    
    print(request.method)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #Con este metodo vamos a autenticar al usuario y nos va retornar un 
        #objeto username sino hace match nada nos devuelve un none
        user = authenticate(username=username , password=password)
        
        if user:
            #vamos a necesitar la peticion y el usuario al cual se le va generar la sesion
            login(request , user)
            
            #Enviando mensajes del servidor al cliente
            messages.success(request , 'Bienvenido {} '.format(user.username))
            
            print("Usuario autenticado")
            
            #Si en caso nos autenticamos ahora tenemos que redirigirnos a la página de inicio
            return redirect('index')
              
        else:
            
            messages.error(request , 'Usuario o contraseña no valido')
            print("Usuario no autenticado")
        
        print('El usuario es {} y el password {} '.format(username,password))
    
    return render(request, 'users/login.html' , {
        
    })


# ()   {}  <!--  -->
def logout_view(request):
    logout(request)
    messages.success(request , 'Sesión cerrada exitosamente')
    return redirect('login')






