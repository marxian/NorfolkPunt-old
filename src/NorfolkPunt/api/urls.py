from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BoatHandler

boat_handler = Resource(BoatHandler)

urlpatterns = patterns('',
   url(r'^boat/(?P<boat_slug>[^/]+)/', boat_handler),
   url(r'^boats/', boat_handler),
)
