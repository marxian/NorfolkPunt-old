from django.db import models
from django.template.defaultfilters import slugify, truncatewords
from datetime import datetime
from photologue.models import ImageModel
from licenses.models import License


YEAR_CHOICES = [(x,x) for x in list(reversed(range(1890, 2020)))]

def slugify_uniquely(value, model, slugfield="slug"):
        """Returns a slug on a name which is unique within a model's table

        This code suffers a race condition between when a unique
        slug is determined and when the object with that slug is saved.
        It's also not exactly database friendly if there is a high
        likelyhood of common slugs being attempted.

        A good usage pattern for this code would be to add a custom save()
        method to a model with a slug field along the lines of:

                from django.template.defaultfilters import slugify

                def save(self):
                    if not self.id:
                        # replace self.name with your prepopulate_from field
                        self.slug = slugify_uniquely(self.name, self.__class__)
                super(self.__class__, self).save()

        Original pattern discussed at
        http://www.b-list.org/weblog/2006/11/02/django-tips-auto-populated-fields
        """
        suffix = 0
        potential = base = slugify(value)
        while True:
                if suffix:
                        potential = "-".join([base, str(suffix)])
                if not model.objects.filter(**{slugfield: potential}).count():
                        return potential
                # we hit a conflicting slug, so bump the suffix & try again
                suffix += 1

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    website = models.URLField(verify_exists=False, blank=True)
    
    def __unicode__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
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
    name = models.CharField(max_length=50)
    sail_number = models.IntegerField(blank=True)
    loa = models.FloatField(blank=True, null=True)
    handicap = models.IntegerField(blank=True, null=True)
    construction = models.ForeignKey(Construction, blank=True, related_name='examples')
    year_built = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    owners = models.ManyToManyField(Person, blank=True, through='Ownership')  
    builder = models.ForeignKey(Boatbuilder, blank=True, related_name='built')
    design = models.ForeignKey(Design, blank=True, related_name='examples')
    previous_names = models.CharField(max_length=100, blank=True)
    preferred_pic = models.ForeignKey('Picture', blank=True, null=True)
    
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-sail_number']
        unique_together = (("name", "sail_number"),)
   
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.name + '-' + str(self.sail_number))
        return super(Boat, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('boat_view', [self.slug])
    
    @property
    def gallery(self):

        pics = Picture.objects.filter(boats__id=self.id).annotate(num_boats=models.Count('boats')).order_by('num_boats')
        listing = pics.all()
        return [x for x in listing]


    
class Note(models.Model):
    text = models.TextField()
    refers_to = models.ForeignKey(Boat, related_name='notes')

  
class Ownership(models.Model):
    
    boat = models.ForeignKey(Boat, related_name="ownership")
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
        if not self.owned_from and not self.owned_to:
            return "%s (at some point)" % (self.owner)

class Picture(ImageModel):

    title = models.CharField('title', max_length=100)
    
    slug = models.SlugField(editable=False, unique=True)
    
    caption = models.TextField('caption', blank=True)
    added = models.DateTimeField('date added', default=datetime.now, editable=False)
    created = models.DateField(blank=True)    
    boats = models.ManyToManyField(Boat, blank=True, through='BoatDepiction', related_name='pictures') 
    people = models.ManyToManyField(Person, blank=True, through='PersonDepiction', related_name='pictures')
    event = models.ForeignKey('events.Event', blank=True, null=True, related_name="gallery")
    
    license = models.ForeignKey(License, blank=True, related_name="media")
    attribution = models.ForeignKey(Person, blank=True, related_name="photographs")
    
    @property
    def depiction_count(self):
        return self.boats.count() + self.people.count()
    
    def __unicode__(self):
        return truncatewords(self.title, 8)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify_uniquely(self.title, self.__class__)
        return super(Picture, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('picture_view', [self.slug])

        
class Depiction(models.Model):
    class Meta:
        abstract = True
    image = models.ForeignKey(Picture)
    top = models.IntegerField(blank=True, null=True)
    left = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
        
class BoatDepiction(Depiction):
    type = 'boats'
    target = models.ForeignKey(Boat, related_name="depictions")

class PersonDepiction(Depiction):
    type = 'people'
    target = models.ForeignKey(Person, related_name="depictions")


    

