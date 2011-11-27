from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def rules(request):
    return render_to_response('puntsite/rules.html', 
                              {},
                              context_instance=RequestContext(request))
    
def history(request):
    return render_to_response('puntsite/history.html', 
                              {},
                              context_instance=RequestContext(request))
    
def home(request):
    return render_to_response('puntsite/home.html',
                              {},
                              context_instance=RequestContext(request))