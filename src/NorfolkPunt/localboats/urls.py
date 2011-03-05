from django.conf.urls.defaults import *

urlpatterns = patterns('localboats.views',
    url(r'^$', 'index'),
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', 'boat', name="boat_view"),
)
