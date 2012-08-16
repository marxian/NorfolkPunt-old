from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from localboats.models import Boat, Picture
from localboats.events.models import Event
import datetime

def rules(request):
    return render_to_response('puntsite/rules.html', 
                              {},
                              context_instance=RequestContext(request))
    
def history(request):
    return render_to_response('puntsite/history.html', 
                              {},
                              context_instance=RequestContext(request))
    
def home(request):
    all_pics = Picture.objects.order_by('?')[:10]
    landscapes = [x for x in all_pics if x.get_display_size()[0] > x.get_display_size()[1]]
    today = datetime.date.today()
    next_event = Event.objects.filter(
        start__gte=today, # Starting next
    ).order_by('start')[0]
    return render_to_response('puntsite/home.html',
                              {
                                "slides": landscapes,
                                "event": next_event
                              },
                              context_instance=RequestContext(request))