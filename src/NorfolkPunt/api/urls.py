from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BoatHandler, BoatDepictionHandler, TagLookupHandler, PersonDepictionHandler

boat_handler = Resource(BoatHandler)
boat_depiction_handler = Resource(BoatDepictionHandler)
person_depiction_handler = Resource(PersonDepictionHandler)
tag_lookup_handler = Resource(TagLookupHandler)

urlpatterns = patterns('',
   url(r'^boats/depictions/', boat_depiction_handler),                    
   url(r'^boat/(?P<boat_slug>[^/]+)/depictions/', boat_depiction_handler),
   url(r'^people/depictions/', person_depiction_handler),                    
   url(r'^person/(?P<person_slug>[^/]+)/depictions/', person_depiction_handler),
   url(r'^boat/(?P<boat_slug>[^/]+)/', boat_handler),
   url(r'^boats/', boat_handler),
   url(r'^lookup', tag_lookup_handler),
   
)
