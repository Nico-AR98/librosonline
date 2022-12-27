"""
WSGI config for librosonline project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
import os
import sys

path = '/var/www/librosonline'

if path not in sys.path:
    sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"]="librosonline"

application = get_wsgi_application()