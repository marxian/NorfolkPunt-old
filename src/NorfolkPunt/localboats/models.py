from django.db import models

YEAR_CHOICES = [(x,x) for x in range(1890, 2020)]

class Person(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class Boat(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    loa = models.FloatField(blank=True, null=True)
    handicap = models.IntegerField(blank=True, null=True)
    construction = models.CharField(max_length=50)
    year_built = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    owners = models.ManyToManyField(Person, blank=True, through='Ownership')  
    builder = models.ForeignKey(Person, blank=True, related_name='built')
    designer = models.ForeignKey(Person, blank=True, related_name='designed')
    
    def __unicode__(self):
        return self.name
    
class Ownership(models.Model):
    
    boat = models.ForeignKey(Boat)
    owner = models.ForeignKey(Person)
    owned_from = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    owned_to = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    
    def __unicode__(self):
        return "%s (%s - %s)" % (self.owner, self.owned_from, self.owned_to)