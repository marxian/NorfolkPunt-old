from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('puntsite.views',
	url(r'^contact/thanks', 'thanks', 
        name="thanks"),
    url(r'^contact/$', 'contact', 
        name="contact"),
    url(r'^technical/$', 'technical', 
        name="technical"),
    url(r'^history/$', 'history', 
        name="history"),
    url(r'^', 'home', name="home"),
    
)