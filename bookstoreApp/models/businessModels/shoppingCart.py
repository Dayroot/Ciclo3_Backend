from django.db import models
from .. import User

class ShoppingCart(models.Model):
    customer = models.ForeignKey(User, related_name='shoppingCart', on_delete=models.CASCADE)