from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('puntsite.views',
    
    url(r'^technical/$', 'technical', 
        name="technical"),
    url(r'^history/$', 'history', 
        name="history"),
    url(r'^', 'home', name="home"),
    
)