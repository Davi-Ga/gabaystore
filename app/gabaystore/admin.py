from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cloth)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)