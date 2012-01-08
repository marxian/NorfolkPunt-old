from django.db import models


    
class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=140)
    body = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title 
    


    
    
    
