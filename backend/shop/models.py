from django.db import models
from django.contrib.auth.models import User
from userManager.models import BasicUser,Address
# Category,Product,Wishlist,WishListItems,Cart,CartItems,ProductReview
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Product(models.Model):
	category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	#images
	description = models.TextField(null=True,blank=True)
	price = models.FloatField(null=True,blank=True)
	stock = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
	user = models.OneToOneField(BasicUser,on_delete=models.CASCADE,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class WishListItem(models.Model):
	wish_list = models.ForeignKey(Wishlist,related_name='items',on_delete=models.CASCADE,null=True,blank=True)
	product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Cart(models.Model):
	user = models.OneToOneField(BasicUser,on_delete=models.CASCADE,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE,null=True,blank=True)
	product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class ProductReview(models.Model):
	user = models.ForeignKey(BasicUser,related_name='product_reviews',on_delete=models.DO_NOTHING,null=True,blank=True)
	product = models.ForeignKey(Product,related_name="reviews",on_delete=models.DO_NOTHING,null=True,blank=True)
	ratings = models.FloatField(null=True,blank=True)#set cieling value as 5
	comment = models.TextField(null=True,blank=True)
	#images
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	


