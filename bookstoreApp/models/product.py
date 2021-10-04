from django.db import models

class Product(models.Model):
    provider_name = models.CharField('Provider', max_length = 45)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)