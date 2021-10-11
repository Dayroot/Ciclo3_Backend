from django.db import models

class Product(models.Model):
    description= models.CharField('Description', max_length=150, blank=True, null=True)
    provider_name = models.CharField('Provider', max_length = 45, blank=True, null=True)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0) 