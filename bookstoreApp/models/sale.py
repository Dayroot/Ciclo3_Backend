from django.db import models
from .product import Product
from .user import User


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='Sales', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Purchases', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)