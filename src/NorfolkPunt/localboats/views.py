from models import Boat, Picture, BoatDepiction
from django.shortcuts import render_to_response, get_object_or_404
from forms import BoatDepictionForm
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse
import json



def boats(request):
    boats = Boat.objects.all()
    
    # Build a list of unique values for Design for the filter list
    # Surely there's abetter way?
    design_types = {}
    for boat in boats:
        design_types[str(boat.design)] = ''
    designs = sorted(design_types.keys())
    
    return render_to_response('localboats/boats.html', {'boats':boats,
                                                              'designs':designs})
def boat(request, slug):
    boat = get_object_or_404(Boat, slug=slug)
    return render_to_response('localboats/boat.html', {'boat': boat})

def pictures(request):
    pictures = Picture.objects.all()
    return render_to_response('localboats/pictures.html', {'pictures':pictures})

def picture(request, slug):
    picture = get_object_or_404(Picture, slug=slug)
    boat_depiction_form = BoatDepictionForm(initial={'image':picture.id})
    return render_to_response('localboats/picture.html', 
                              {'picture': picture,
                               'boat_depictions':BoatDepiction.objects.filter(image=picture),
                               'boat_depiction_form':boat_depiction_form},
                               context_instance=RequestContext(request))
    
def picture_depictions(request, slug):

    picture = get_object_or_404(Picture, slug=slug)
    depictions = BoatDepiction.objects.filter(image=picture)
    
    data = []
    for dep in depictions:
        data.append({'DATE':'',
                     'ID':dep.id,
                     'LINK':'',
                     'AUTHOR':'',
                     'LEFT':dep.left,
                     'TOP':dep.top,
                     'WIDTH':dep.width,
                     'HEIGHT':dep.height,
                     'NOTE':dep.boat.name})

    return HttpResponse(json.dumps(data), mimetype='application/json')

    