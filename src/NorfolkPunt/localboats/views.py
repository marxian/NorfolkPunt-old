from models import Boat
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    boats = Boat.objects.all()
    design_types = {}
    for boat in boats:
        design_types[str(boat.design)] = ''
    designs = sorted(design_types.keys())
    return render_to_response('localboats/boats_index.html', {'boats':boats,
                                                              'designs':designs})

def boat(request, slug):
    boat = get_object_or_404(Boat, slug=slug)
    return render_to_response('localboats/boat.html', {'boat': boat})

    


