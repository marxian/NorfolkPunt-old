from django.db import models


YEAR_CHOICES = [(x,x) for x in list(reversed(range(1890, 2020)))]

class Agent(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    class Meta:
        abstract = True
        ordering = ['name']  
    def __unicode__(self):
        return self.name

class Person(Agent):
    class Meta:
        ordering = ['name']
        verbose_name = 'person'
        verbose_name_plural = 'people'

class Boatbuilder(Agent):
    pass
    
class Designer(Agent):
    pass
    
class Design(models.Model):
    name = models.CharField(max_length=50)
    designer = models.ForeignKey(Designer, blank=True, related_name='designed')
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
    
class Construction(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Construction Type'
    
    def __unicode__(self):
        return self.name
    
class Boat(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    loa = models.FloatField(blank=True, null=True)
    handicap = models.IntegerField(blank=True, null=True)
    construction = models.ForeignKey(Construction, blank=True, related_name='examples')
    year_built = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    owners = models.ManyToManyField(Person, blank=True, through='Ownership')  
    builder = models.ForeignKey(Boatbuilder, blank=True, related_name='built')
    design = models.ForeignKey(Design, blank=True, related_name='examples')
    
    class Meta:
        ordering = ['-number']
    
    def __unicode__(self):
        return self.name

        
    
class Ownership(models.Model):
    
    boat = models.ForeignKey(Boat)
    owner = models.ForeignKey(Person)
    owned_from = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    owned_to = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    
    class Meta:
        ordering = ['-owned_from', '-owned_to']
    
    def __unicode__(self):
        if self.owned_from and self.owned_to:
            return "%s (%s - %s)" % (self.owner, self.owned_from, self.owned_to)
        if self.owned_from and not self.owned_to:
            return "%s (%s to present)" % (self.owner, self.owned_from)
        if not self.owned_from and self.owned_to:
            return "%s (until %s)" % (self.owner, self.owned_to)