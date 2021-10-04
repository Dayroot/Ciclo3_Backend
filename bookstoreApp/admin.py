from django.contrib import admin
from .models.employee import Employee
from .models.workArea import WorkArea
from .models.user import User

admin.site.register(Employee)
admin.site.register(WorkArea)
admin.site.register(User)

