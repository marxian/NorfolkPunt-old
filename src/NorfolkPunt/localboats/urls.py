from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('localboats.views',
    # Picture Views
    url(r'^pictures/$', 'pictures', 
        name="localboats:pictures_index"),
    url(r'^pictures/(?P<slug>[a-zA-Z0-9_.-]+)/annotations/$', 'picture_depictions', 
        name="picture_depictions"),
    url(r'^pictures/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'picture', 
        name="picture_view"),
    # Boat Views
    url(r'^$', 'boats', 
        name="localboats:boats_index"),
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', 'boat', 
        name="boat_view"),
    
)
