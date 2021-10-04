from django.contrib import admin
from .models.employee import Employee
from .models.workArea import WorkArea
from .models.user import User

from models.magazine import Magazine
from models.book import Book
from models.product import Product
from models.sale import Sale
from models.reservation import Reservation

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(WorkArea)

admin.site.register(Magazine)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Reservation)


