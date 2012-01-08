from django.conf.urls.defaults import include, url, patterns
                       

urlpatterns = patterns('localboats.views',
    # Picture Views
    url(r'^pictures/$', 'pictures', 
        name="pictures_index"),
    url(r'^pictures/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'picture', 
        name="picture_view"),
    # Boat Views
    url(r'^boats/$', 'boats', 
        name="boats_index"),
    url(r'^boats/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'boat', 
        name="boat_view"),
    
    
    
)
