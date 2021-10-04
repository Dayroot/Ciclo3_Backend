from django.db import models
from .workArea import WorkArea
from .user import User

class Employee(models.Model):
    
    user= models.OneToOneField(User, related_name='employees', on_delete= models.CASCADE)
    work_area = models.ForeignKey(WorkArea, on_delete= models.PROTECT, related_name='employees')
    salary = models.BigIntegerField('Salary')
    is_seller = models.BooleanField(default=False)
    is_inventory_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)