import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

application = get_wsgi_application()



#MADE BY SABAU EDUARD