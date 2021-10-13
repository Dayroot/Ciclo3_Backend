from django.db import models
from .. import User

class ShoppingCart(models.Model):
    customer = models.ForeignKey(User, related_name='shoppingCart', on_delete=models.CASCADE)
    datetime= models.DateTimeField(auto_now=True)
    is_sale = models.BooleanField(default=False)
    is_shoppingCart = models.BooleanField(default=False)