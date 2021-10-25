from django.db import models
from .. import User

class Invoice(models.Model):
    customer = models.ForeignKey(User, related_name='invoice', on_delete=models.CASCADE)
    datetime= models.DateTimeField(auto_now=True)