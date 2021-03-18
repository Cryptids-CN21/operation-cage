import datetime
from django.db import models
from django.utils import timezone 

class Cryptid(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    image = models.ImageField(upload_to="cryptids/")
    discovery_date = models.DateField(null=True)

    def __str__(self):
        return self.text



class Location(models.Model):
    cryptids = models.ManyToManyField(Cryptid, related_name="locations")
    text = models.CharField(max_length=200)
    

    def __str__(self):
        return self.text