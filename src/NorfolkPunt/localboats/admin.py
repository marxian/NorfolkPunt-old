from django.contrib import admin

from models import *

class OwnershipInline(admin.StackedInline):
    model = Ownership
    extra = 0
    
class NotesInline(admin.StackedInline):
    model = Note
    extra = 0

class BoatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'sail_number', 'year_built', 'previous_names']}),
        ('Details', {'fields': ['handicap', 'loa', 'design', 'builder', 'construction'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'sail_number')


    inlines = [OwnershipInline, NotesInline]
    
    class Media:
        """Collapse the inline forms for Ownerships"""
        js = ['/site_media/js/collapsed_stacked_inlines.js']
        

        
class BoatDepictionInline(admin.StackedInline):
    model = BoatDepiction
    fields = ['target']
    extra = 0
    
class PersonDepictionInline(admin.StackedInline):
    model = PersonDepiction
    fields = ['target']
    extra = 0
    
class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['title', 'caption', 'created', 'image', 'license', 'attribution']})
    ]
    list_display = ('title','caption','added','created','depiction_count','admin_thumbnail')
    inlines = [BoatDepictionInline, PersonDepictionInline]


admin.site.register(Boat, BoatAdmin)
admin.site.register(Place)
admin.site.register(Person)
admin.site.register(Design)
admin.site.register(Designer)
admin.site.register(Boatbuilder)
admin.site.register(Construction)
admin.site.register(Picture, PictureAdmin)
