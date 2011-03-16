from piston.handler import BaseHandler, AnonymousBaseHandler
from localboats.models import Boat, BoatDepiction, Person
from localboats.forms import BoatDepictionForm
from piston.utils import validate, rc

class BoatHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Boat
    fields = ('name',
              'sail_number',
              'loa',
              'handicap',
              'year_built',
              'slug',
              ('builder', ('name',),),
              ('construction', ('name',),),
              ('design', ('name', 'designer_id'),),
              'previous_names',
              )
    
    def read(self, request, boat_slug=None):
        """
        Returns a single post if `blogpost_id` is given,
        otherwise a subset.

        """
        base = Boat.objects
        
        if boat_slug:
            return base.get(slug=boat_slug)
        else:
            return base.all()
        
class TagLookupHandler(AnonymousBaseHandler):
    """ Short form boat and person lookups for autocomplete style searches """
    allowed_methods = ('GET',)
    
    def read(self, request):
        """
        Returns items matching terms

        """
        term = request.GET.get('term', None)
        data = []
        if term:
            boats = Boat.objects.filter(name__icontains=term)
            people = Person.objects.filter(name__icontains=term)
        
        
            for boat in boats:
                data.append({'label':boat.name, 'id':boat.id, 'category':'Boats'})
            for person in people:
                data.append({'label':person.name, 'id':person.name, 'category':'People'})
            
        return data
        
class BoatDepictionHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = BoatDepiction
    
    def read(self, request, boat_slug=None, depiction_id=None):
        if boat_slug:
            boat = Boat.objects.get(slug=boat_slug)
            return BoatDepiction.objects.filter(boat=boat)
        elif depiction_id:
            return BoatDepiction.objects.get(pk=depiction_id)
        else:
            return BoatDepiction.objects.all()
        
    @validate(BoatDepictionForm)
    def create(self, request):
        request.form.save()
        return rc.CREATED
        
        

        
        
        
        

