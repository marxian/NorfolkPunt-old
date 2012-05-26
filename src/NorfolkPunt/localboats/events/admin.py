from django.contrib import admin

from models import *

class RacePositionInline(admin.StackedInline):
    model = RacePosition
    extra = 0
    
class RaceTrophyInline(admin.StackedInline):
    model = RaceTrophy
    extra = 0
    
class RaceResultAdmin(admin.ModelAdmin):
    inlines = [RacePositionInline, RaceTrophyInline]
    


class EventAdmin(admin.ModelAdmin):
    
    class Media:
        """Collapse the inline forms for Ownerships"""
        js = ['/site_media/js/collapsed_stacked_inlines.js']

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
admin.site.register(EventFlag)
admin.site.register(RaceResult, RaceResultAdmin)
