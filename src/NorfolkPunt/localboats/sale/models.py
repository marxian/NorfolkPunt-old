from django.db import models
from localboats.models import Boat

    
class Sale(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=140)
    contact = models.TextField(blank=True)
    details = models.TextField(blank=True)
    boat = models.ForeignKey(Boat, blank=True, related_name="forsale")
    
    def __unicode__(self):
        return self.title 
    


    
    
    
