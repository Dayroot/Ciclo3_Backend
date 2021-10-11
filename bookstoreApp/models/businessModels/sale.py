from django.db import models
from .. import Product
from .. import User
class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sold_products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    client = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    datetime= models.DateTimeField(auto_now=True)