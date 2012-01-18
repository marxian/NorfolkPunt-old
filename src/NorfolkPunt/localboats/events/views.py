from models import Event, EventType, RaceResult
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def events(request):
    events = Event.objects.all()
    event_types = EventType.objects.all()
    
    return render_to_response('localboats/events/events.html', 
                              {'events':events,
                               'event_types':event_types},
                               context_instance=RequestContext(request))
    
def event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    results = event.results.all()
    
    return render_to_response('localboats/events/event.html', 
                              {'event':event,
                               'results':results},
                               context_instance=RequestContext(request))
    

