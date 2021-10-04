from django.db import models 
from .product import Product

class Magazine(models.Model):

    product = models.OneToOneField(Product, related_name='Magazines', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField('Name', max_length = 45)
    edition = models.IntegerField(default=0)
    publication_date = models.DateTimeField()  
    issn = models.CharField('ISSN', max_length = 8)
    editorial = models.CharField('Editorial', max_length = 30)