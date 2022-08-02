from distutils.command.upload import upload
from statistics import mode
from django.db import models


# Create your models here.

class Tracks(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    track_banner=models.ImageField(null=True,blank=True,upload_to='trackImages/')
    title=models.CharField(max_length=200,blank=False)

    class Meta:
        ordering=['created']

class Product(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(null=True,blank=True,upload_to='productImages')
    price=models.IntegerField()

    class Meta:
        ordering=['created']
    
