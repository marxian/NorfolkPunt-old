from django.db import models
from django.template.defaultfilters import slugify, truncatewords
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import ordinal 

from localboats.models import slugify_uniquely, Boat, Person, Place
    

class EventType(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(EventType, related_name="events")
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Place, related_name="hosts")
    postcode = models.CharField(max_length=10, blank=True)
    
    def __unicode__(self):
        return self.name + ' (%s)' % (self.start.strftime('%Y'))
    
class RaceResult(models.Model):
    event = models.ForeignKey(Event, related_name='results')
    report = models.TextField(blank=True)
    full_results = models.FileField(upload_to='results', blank=True)
    
    def __unicode__(self):
        return str(self.event) + ' Results'

class RacePosition(models.Model):
    position = models.IntegerField()
    boat = models.ForeignKey(Boat, related_name="race_positions")
    helm = models.ForeignKey(Person, related_name="helming_positions")
    crew = models.ForeignKey(Person, related_name="crewing_positions")
    points = models.IntegerField(blank=True, null=True)
    raceresult = models.ForeignKey(RaceResult, related_name='positions')
    
    def __unicode__(self):
        return '%s - %s' % (ordinal(self.position), self.boat.name)
    

    
    
    
