from django.conf.urls.defaults import include, patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Serve site_media while in development             
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    # Serve uploaded media while in development
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Use localboats to provide boat, picture, boatlisting and gallery views
    (r'^', include('localboats.urls')),
    
    # Use puntsite to provide semi statis views like home, rules, history
    (r'^', include('puntsite.urls')),
    
    # Use the piston based api app to provide the NorfolkPunt API
    (r'^api/', include('api.urls')),
)
