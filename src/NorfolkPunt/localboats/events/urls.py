from django.conf.urls.defaults import url, patterns
                       

urlpatterns = patterns('localboats.events.views',
    # Event Views
    url(r'^events/$', 'events', 
        name="events_index"),
    url(r'^events/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'event', 
        name="event_view"),
)
