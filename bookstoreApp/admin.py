from django.contrib import admin
from .models.employee import Employee
from .models.workArea import WorkArea

admin.site.register(Employee)
admin.site.register(WorkArea)

