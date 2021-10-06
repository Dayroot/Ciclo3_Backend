from django.db import models
from .product import Product   

class Book(models.Model):

    product = models.OneToOneField(Product, related_name='Books', on_delete=models.CASCADE, primary_key=True)
    title = models.CharField('Title', max_length = 45, blank=True, null=True)
    author = models.CharField('Autor', max_length = 45, blank=True, null=True)
    publication_date = models.DateTimeField( blank=True, null=True)
    isbn = models.CharField('ISSN', max_length = 13, blank=True, null=True)
    editorial = models.CharField('Editorial', max_length = 30, blank=True, null=True)