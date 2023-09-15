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


#Con esto vamos a usar el modelo User para crear usuarios
from django.contrib.auth.models import User



from .forms import RegisterForm

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


def register(request):
    #vamos a crear una instancia de forms
    #Cuando le pasamos un diccionario estos valores son 
    #los que se pintan en el formulario
    #form=RegisterForm({
    #    'username' : 'Jairo',
    #    'email':'jairo@gmail.com'
    #})
    
    #Con esto yo le estoy  indicando a django
    #que si la peticion es por método post entonces se genera un 
    #Formulario con los datos que el cliente envia
    #Sino los genera con el campo vacio
    form=RegisterForm(
        request.POST or None
    )
    
    
    #is_validad nos permite conocer si el formulario es valido o no
    #cleaned_data es un diccionario
    if request.method == 'POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        
        #El método create user se encarga de encriptar a la contraseña
        #Este métodos crea usuarios pero no con permiso de administrador
        user = User.objects.create_user(username,email,password)
        
        if user:
            #Pero debemos de crear la session
            login(request,user)
            messages.success(request , 'Usuario creado exitosamente') 
            return redirect('index')
        
        
        print(username)
        print(email)
        print(password)
        
    
    #Este es el formulario que se muestra ni bien ingreso a la URL
    #Ya dentro del formulario se va aplicar los metodo arriba codificados
    return render(request,'users/register.html',{
        'form':form
    })




