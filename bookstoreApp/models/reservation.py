from django.db import models
from .productModels import Product
from .user import User

class Reservation(models.Model):
    product = models.ForeignKey(Product, related_name='reserved_products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    datetime= models.DateTimeField(auto_now=True)