from django.db import models

class WorkArea(models.Model):
    
    name =  models.CharField('work area name', max_length=30)