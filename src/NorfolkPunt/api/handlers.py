from piston.handler import BaseHandler, AnonymousBaseHandler
from localboats.models import Boat

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
        

