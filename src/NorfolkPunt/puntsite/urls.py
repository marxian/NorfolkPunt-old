from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('puntsite.views',
    url(r'^', 'home', name="home"),
    url(r'^rules/$', 'rules', 
        name="rules"),
    url(r'^history/$', 'history', 
        name="history"),
    
)