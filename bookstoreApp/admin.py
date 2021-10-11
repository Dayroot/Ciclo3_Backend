from django.contrib import admin
from .models import Employee
from .models import WorkArea
from .models import User

from .models import Magazine
from .models import Book
from .models import Product
from .models import Sale
from .models import Reservation

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(WorkArea)

admin.site.register(Magazine)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Reservation)


