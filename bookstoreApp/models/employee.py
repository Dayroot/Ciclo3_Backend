from django.db import models
from .workArea import WorkArea
from .user import User

class Employee(models.Model):

    user= models.OneToOneField(User, related_name='employees', on_delete= models.CASCADE, primary_key=True)
    work_area = models.ForeignKey(WorkArea, to_field= 'name', db_column= 'work_area_name', on_delete= models.PROTECT, related_name='employees',blank=True, null=True)
    salary = models.BigIntegerField('Salary', blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    is_inventory_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    PARENT_MODEL= User
    PARENT_MODEL_NAME = 'user'