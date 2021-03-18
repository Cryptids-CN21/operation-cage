import datetime
from django.db import models
from django.utils import timezone 

class Cryptid(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    image = models.ImageField(upload_to="cryptids/")

    def __str__(self):
        return self.text


    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Location(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    discoveryDate = models.DateField(null=True)

    def __str__(self):
        return self.text