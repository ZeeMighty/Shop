from django.db import models

class Good(models.Model):
    Name = models.CharField(max_length = 150)
    Type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    Available = models.CharField(max_length = 50)
    Photo = models.ImageField(upload_to = 'clothes_photos')
    Price = models.IntegerField(default = '0')
    Discount = models.IntegerField(default = '0')
    Size = models.ManyToManyField('Size')
    URL = models.CharField(max_length = 50, default = " ")


    def __str__(self):
        return self.Name

#class GetObjectManeger(models.Manager):
#    def all(self, *args, **kwargs):
#        return super(ArticleManager, self).get_queryset().filter()

class Type(models.Model):
    type = models.CharField(max_length = 50, default = " ")

    def __str__(self):
        return self.type

class Size(models.Model):
    size = models.CharField(max_length = 150)

    def __str__(self):
        return self.size


class Good_Get(models.Model):
#    Name = models.CharField(max_length = 150)
#    Price = models.IntegerField(default = '0')
#    Photo = models.ImageField(upload_to = 'clothes_photos')
    Size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name
