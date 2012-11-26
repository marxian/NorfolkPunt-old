from models import Event, EventType, RaceResult
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime

def events(request):
    events = Event.objects.all()
    event_types = EventType.objects.all()
    past = events.filter(start__lte=datetime.now()).order_by('-start')
    future = events.filter(start__gte=datetime.now()).order_by('start')
    return render_to_response('localboats/events/events.html', 
                              {'events':events,
                               'past': past,
                               'future': future,
                               'event_types':event_types},
                               context_instance=RequestContext(request))
    
def event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    results = event.results.all()
    gallery = event.gallery.all().order_by('?')
    return render_to_response('localboats/events/event.html', 
                              {'event':event,
                               'results':results,
                               'gallery': gallery
                               },
                               context_instance=RequestContext(request))
    

