from django.conf.urls.defaults import patterns

urlpatterns = patterns('localboats.views',
    (r'^$', 'index'),
    (r'^(?P<boat_number>\d+)/$', 'boat'),
)
