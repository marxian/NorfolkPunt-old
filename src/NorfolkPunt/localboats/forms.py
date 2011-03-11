from django.forms import ModelForm
from models import BoatDepiction
from django.shortcuts import redirect


class BoatDepictionForm(ModelForm):
    class Meta:
        model = BoatDepiction

def add_boat_depiction(request):
    form = BoatDepictionForm(request.POST)
    new_depiction = form.save()
    return redirect(new_depiction.image)