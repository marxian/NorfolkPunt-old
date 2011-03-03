
from models import Boat
from django.shortcuts import render_to_response, get_object_or_404





def index(request):
    boats = Boat.objects.all()
    return render_to_response('localboats/boats_index.html', {'boats':boats})

def boat(request, boat_number):
    boat = get_object_or_404(Boat, pk=boat_number)
    return render_to_response('localboats/boat.html', {'boat': boat})

    


