from django.db import models

class Product(models.Model):
    editorial = models.CharField('editorial', max_length = 50, blank=True, null=True)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField('Description', blank=True, null=True)
    type = models.CharField('type', max_length=15, blank=True, null=True)
    publication_date = models.DateField('date publication', blank=True, null=True)
    image_url = models.CharField('image url', max_length = 50, blank=True, null=True)
   
    
     