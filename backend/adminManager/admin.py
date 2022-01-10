from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import FAQCategory,FAQSubCategory,FAQ,BlogCategory,Blog,Testimonial


# Register your models here.
class EcomAdminSite(AdminSite):
	site_header = 'Ecom Admin Interface'
	site_title = 'Ecom Administration'
	index_title = 'Ecom Administration'
	site_url = None

admin_site = EcomAdminSite(name="EcomManager")

#regiteration
admin_site.register(FAQCategory)
admin_site.register(FAQSubCategory)
admin_site.register(FAQ)
admin_site.register(BlogCategory)
admin_site.register(Blog)
admin_site.register(Testimonial)
