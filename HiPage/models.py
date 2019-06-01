from django.db import models

class Good(models.Model):
    Name = models.CharField(max_length = 150)
    Available = models.CharField(max_length = 50)
    Photo = models.ImageField(upload_to = 'clothes_photos')
#    Size в другой модели и сюда подключить

def _str_(self):
    return self.Name

class Size(models.Model):
    size = models.CharField(max_length = 150)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, null=True)

def _str_(self):
    return self.size
