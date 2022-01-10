from django.contrib import admin
from adminManager.admin import admin_site
from .models import BasicUser,Address

# Register your models here.
admin_site.register(BasicUser)
admin_site.register(Address)
