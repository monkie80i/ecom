from django.contrib import admin
from adminManager.admin import admin_site
from .models import Category,Product,Wishlist,WishListItem,Cart,CartItem,ProductReview


# Register your models here.
admin_site.register(Category)
admin_site.register(Product)
admin_site.register(Wishlist)
admin_site.register(WishListItem)
admin_site.register(Cart)
admin_site.register(CartItem)
admin_site.register(ProductReview)

