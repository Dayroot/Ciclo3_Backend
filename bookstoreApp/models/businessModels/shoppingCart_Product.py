from django.db import models
from .. import Product
from . import ShoppingCart

class ShoppingCart_Product(models.Model):
    product = models.ForeignKey(Product, related_name='shoppingCart_product_inventory', on_delete=models.CASCADE)
    shoppingCart = models.ForeignKey(ShoppingCart, related_name='shoppingCart_product', on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)