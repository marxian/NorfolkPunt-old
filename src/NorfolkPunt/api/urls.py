from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BoatHandler, BoatDepictionHandler

boat_handler = Resource(BoatHandler)
boat_depiction_handler = Resource(BoatDepictionHandler)

urlpatterns = patterns('',
   url(r'^boats/depictions/', boat_depiction_handler),                    
   url(r'^boat/(?P<boat_slug>[^/]+)/depictions/', boat_depiction_handler),
   url(r'^boat/(?P<boat_slug>[^/]+)/', boat_handler),
   url(r'^boats/', boat_handler),
   
)
