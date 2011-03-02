from django.contrib import admin
from models import Boat, Person, Ownership

class OwnershipInline(admin.StackedInline):
    model = Ownership
    extra = 0

class BoatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'number', 'year_built']}),
        ('Details', {'fields': ['handicap', 'loa', 'designer', 'builder', 'construction'], 'classes': ['collapse']}),
    ]
    inlines = [OwnershipInline]
    
    class Media:
        js = ['/site_media/js/collapsed_stacked_inlines.js']

admin.site.register(Boat, BoatAdmin)
admin.site.register(Person)
