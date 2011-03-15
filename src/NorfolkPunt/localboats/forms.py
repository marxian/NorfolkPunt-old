from django.forms import ModelForm, HiddenInput
from models import BoatDepiction
from django.shortcuts import redirect


class BoatDepictionForm(ModelForm):
    
    class Meta:
        model = BoatDepiction
        widgets = {
            'image': HiddenInput(),
            'top': HiddenInput(),
            'left': HiddenInput(),
            'height': HiddenInput(),
            'width': HiddenInput(),
        }


        
