from django.db import models
from .product import Product   

class Book(models.Model):

    product = models.OneToOneField(Product, related_name='Books', on_delete=models.CASCADE, primary_key=True)
    title = models.CharField('Title', max_length = 45)
    autor = models.CharField('Autor', max_length = 45)
    publication_date = models.DateTimeField()
    isbn = models.CharField('ISSN', max_length = 13)
    editorial = models.CharField('Editorial', max_length = 30)