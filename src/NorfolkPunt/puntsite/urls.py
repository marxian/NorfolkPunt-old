from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('puntsite.views',
    # Picture Views
    url(r'^rules/$', 'rules', 
        name="rules"),
    url(r'^history/$', 'history', 
        name="history"),
    
)