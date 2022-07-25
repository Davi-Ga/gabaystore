from django.contrib import admin
from .models import Cloth
from .models import Order
from .models import OrderItems

# Register your models here.
admin.site.register(Cloth)
admin.site.register(Order)
admin.site.register(OrderItems)