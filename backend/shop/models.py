from django.db import models
from django.contrib.auth.models import User
from userManager.models import BasicUser,Address
# Category,Product,Wishlist,WishListItems,Cart,CartItems,ProductReview
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True,unique=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ("-created",)

class Product(models.Model):
	category = models.ManyToManyField(Category,related_name='products',blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	#images
	description = models.TextField(null=True,blank=True)
	price = models.FloatField(null=True,blank=True)
	stock = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ("-created",)

class Wishlist(models.Model):
	user = models.OneToOneField(BasicUser,on_delete=models.CASCADE,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def length(self):
		return self.items.count()
	#def __str__(self):
	#	usr =  self.user.user
	#	return usr.first_name+" "+usr.last_name

class WishListItem(models.Model):
	wish_list = models.ForeignKey(Wishlist,related_name='items',on_delete=models.CASCADE,null=True,blank=True)
	product = models.ForeignKey(Product,related_name='wish_list_items',on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#def __str__(self):
	#	return self.

	class Meta:
		ordering = ("-created",)

class Cart(models.Model):
	user = models.OneToOneField(BasicUser,on_delete=models.CASCADE,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#def __str__(self):
	#	return self.

	def total_cost(self):
		total = 0
		for item in self.items.all():
			total = total+item.total_cost()
		return total

	def length(self):
		return self.items.count()

	def clear(self):
		if self.is_deleted:
			return False
		items = self.items.all().filter(is_deleted=False)
		for item in items:
			item.is_active = False
			item.is_deleted = True
			item.save()
		return True

	def is_empty(self):
		return not self.items.all().filter(is_deleted=False).exists()

class CartItem(models.Model):
	cart = models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE,null=True,blank=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_items',null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#def __str__(self):
	#	return self.

	def total_cost(self):
		return self.product.price*self.quantity

	class Meta:
		ordering = ("-created",)

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

	#def __str__(self):
	#	return self.

	class Meta:
		ordering = ("-created",)
	


