import os
import sys
import site

site.addsitedir('/home/norfolkpunt/NorfolkPunt/vpython/lib/python2.5/site-packages')

path = '/home/norfolkpunt/NorfolkPunt/src/'
if path not in sys.path:
    sys.path.append(path)

path2 = '/home/norfolkpunt/NorfolkPunt/src/NorfolkPunt/'
if path2 not in sys.path:
    sys.path.append(path2)

os.environ['DJANGO_SETTINGS_MODULE'] = 'NorfolkPunt.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
