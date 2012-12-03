from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from localboats.models import Boat, Picture
from localboats.sale.models import Sale
from localboats.news.models import News
from localboats.events.models import Event, RaceResult
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
    next_events = Event.objects.filter(
        start__gte=today, # Starting next
    ).order_by('start')
    next_event = len(next_events) and next_events[0] or False

    result = RaceResult.objects.order_by('event__start').reverse()[0]
    
    forsale = Sale.objects.all()

    news = News.objects.order_by('pub_date').reverse()[:3]

    return render_to_response('puntsite/home.html',
                              {
                                "slides": landscapes,
                                "event": next_event,
                                "sales": forsale,
                                "result": result,
                                "news": news
                              },
                              context_instance=RequestContext(request))