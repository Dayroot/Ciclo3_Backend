from django.db import models 
from .product import Product

class Magazine(models.Model):

    product = models.OneToOneField(Product, related_name='Magazines', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField('Name', max_length = 200, blank=True, null=True)
    edition = models.IntegerField(default=0, blank=True, null=True)  
    issn = models.CharField('ISSN', max_length = 8, blank=True, null=True)

    PARENT_MODEL= Product
    PARENT_MODEL_NAME = 'product'