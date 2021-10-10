from django.db import models

class WorkArea(models.Model):
    
    name =  models.CharField('work area name', max_length=30, unique=True)
    
    def __str__(self):
        return self.name