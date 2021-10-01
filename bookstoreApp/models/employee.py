from django.db import models
from django.db.models.deletion import PROTECT
from .person import AbstracBasePerson
from .workArea import WorkArea

class Employee(AbstracBasePerson):
    
    work_area = models.ForeignKey(WorkArea, on_delete= models.PROTECT, related_name='employees')
    salary = models.BigIntegerField('Salary')