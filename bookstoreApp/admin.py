#Staff
from django.contrib import admin
from .models import Employee
from .models import WorkArea
from .models import User

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(WorkArea)

#Products
from .models import Magazine
from .models import Book
from .models import Product

admin.site.register(Magazine)
admin.site.register(Book)
admin.site.register(Product)

#business
from .models import ShoppingCart
from .models import ShoppingCart_Product
from .models import Invoice
from .models import Invoice_Product

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCart_Product)
admin.site.register(Invoice)
admin.site.register(Invoice_Product)

