"""StoreJairo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Aquí se va definir todas las URL del proyecto

from django.contrib import admin
from django.urls import path
from . import views

from django.urls import include

from products.views import ProductListView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('usuarios/login',views.login_views , name='login' ),
    
    path('usuarios/logout',views.logout_view , name='logout' ),
    path('usuarios/registro',views.register , name='register' ),
    
    #path('', views.index , name='index'),
    path('', ProductListView.as_view(), name='index'),
    
    path('render/', views.examplerender , name='render'),
    
    
    path('productos/',include('products.urls'))
]
#recordar que con el include ya podria usar cada url de las aplicaciones sin ningun problema
#Con esto significa que vamos a agregar dichas rutas si estamos en debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






