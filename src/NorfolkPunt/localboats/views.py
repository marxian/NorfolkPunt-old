from models import Boat, Picture, BoatDepiction, PersonDepiction
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext





def boats(request):
    boats = Boat.objects.all()
    # Build a list of unique values for Design for the filter list
    # Surely there's abetter way?
    design_types = {}
    for boat in boats:
        design_types[str(boat.design)] = ''
    designs = sorted(design_types.keys())
    
    return render_to_response('localboats/boats.html', 
                              {'boats':boats,
                               'designs':designs},
                               context_instance=RequestContext(request))
def boat(request, slug):
    boat = get_object_or_404(Boat, slug=slug)
    
    pics = boat.gallery
    has_pics = len(pics)
    main_pic = has_pics and pics[0] or None
    gallery = (has_pics > 1) and pics[1:] or None
    return render_to_response('localboats/boat.html', {'boat': boat, 
                                                       'has_pics':has_pics,
                                                       'main_pic':main_pic,
                                                       'gallery':gallery},
                                                       context_instance=RequestContext(request))

def pictures(request):
    pictures = Picture.objects.all()
    return render_to_response('localboats/pictures.html', {'pictures':pictures},context_instance=RequestContext(request))

def picture(request, slug):
    picture = get_object_or_404(Picture, slug=slug)
    
    boats = BoatDepiction.objects.filter(image=picture)
    people = PersonDepiction.objects.filter(image=picture)

    depictions = [x for x in boats] + [x for x in people]
    return render_to_response('localboats/picture.html', 
                              {'picture': picture,
                               'depictions':depictions},context_instance=RequestContext(request))
    
    