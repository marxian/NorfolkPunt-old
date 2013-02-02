from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from localboats.models import Boat, Picture
from localboats.sale.models import Sale
from localboats.news.models import News
from localboats.events.models import Event, RaceResult
import datetime
from django import forms

def technical(request):
    return render_to_response('puntsite/technical.html', 
                              {},
                              context_instance=RequestContext(request))
    
def history(request):
    return render_to_response('puntsite/history.html', 
                              {},
                              context_instance=RequestContext(request))

class ContactForm(forms.Form):
    recipient = forms.CharField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()

def contact(request):
    contacts = { 
                  "secretary": "nevilleandval@gmail.com",
                  "webmaster": "rupert@neontribe.co.uk"
                }
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            recipient_key = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            recipients = [contacts[recipient_key]]

            recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('puntsite/contact.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('puntsite/thanks.html',
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