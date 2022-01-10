from django.contrib import admin
from adminManager.admin import admin_site
from .models import Order,OrderItem

# Register your models here.
admin_site.register(Order)
admin_site.register(OrderItem)
