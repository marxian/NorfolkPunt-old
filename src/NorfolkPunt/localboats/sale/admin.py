from django.contrib import admin

from models import *




class SaleAdmin(admin.ModelAdmin):
    
    class Media:
        """Collapse the inline forms for Ownerships"""
        js = ['/site_media/js/collapsed_stacked_inlines.js']

admin.site.register(Sale, SaleAdmin)

