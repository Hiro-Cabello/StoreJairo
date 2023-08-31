"""
WSGI config for StoreJairo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

#Archivo que nos va permitir hacer deploy del proyecto a un servidor

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StoreJairo.settings')

application = get_wsgi_application()
