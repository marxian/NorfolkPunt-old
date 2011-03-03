from django.contrib import admin
from models import Boat, Person, Ownership, Design, Designer, Boatbuilder, Construction

class OwnershipInline(admin.StackedInline):
    model = Ownership
    extra = 0

class BoatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'number', 'year_built']}),
        ('Details', {'fields': ['handicap', 'loa', 'design', 'builder', 'construction'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'number')


    inlines = [OwnershipInline]
    
    class Media:
        """Collapse the inline forms for Ownerships"""
        js = ['/site_media/js/collapsed_stacked_inlines.js']

admin.site.register(Boat, BoatAdmin)
admin.site.register(Person)
admin.site.register(Design)
admin.site.register(Designer)
admin.site.register(Boatbuilder)
admin.site.register(Construction)
