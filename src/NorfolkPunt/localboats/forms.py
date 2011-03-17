from django.forms import ModelForm
from models import BoatDepiction, PersonDepiction

class BoatDepictionForm(ModelForm):
    
    class Meta:
        model = BoatDepiction
        
class PersonDepictionForm(ModelForm):
    
    class Meta:
        model = PersonDepiction

        
