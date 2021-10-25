from django.db import models
from .. import Product
from . import Invoice

class Invoice_Product(models.Model):
    product = models.ForeignKey(Product, related_name='invoice_product_inventory', on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, related_name='invoice_product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)