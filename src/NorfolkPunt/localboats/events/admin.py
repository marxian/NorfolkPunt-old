from django.contrib import admin

from models import *

class RacePositionInline(admin.StackedInline):
    model = RacePosition
    extra = 0
    
class RaceResultAdmin(admin.ModelAdmin):
    inlines = [RacePositionInline]


class EventAdmin(admin.ModelAdmin):
    
    class Media:
        """Collapse the inline forms for Ownerships"""
        js = ['/site_media/js/collapsed_stacked_inlines.js']

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
admin.site.register(RaceResult, RaceResultAdmin)