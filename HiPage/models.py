from django.db import models
from django.urls import reverse

class Good(models.Model):
    Name = models.CharField(max_length = 150)
    Available = models.CharField(max_length = 50)
    Photo = models.ImageField(upload_to = 'clothes_photos')
    Price = models.IntegerField(default = '0')
    Discount = models.IntegerField(default = '0')
    Size = models.ManyToManyField('Size')


def _str_(self):
    return self.Name

class Size(models.Model):
    size = models.CharField(max_length = 150)

def _str_(self):
    return self.size
