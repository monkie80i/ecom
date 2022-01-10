from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from userManager.models import BasicUser,Address
# Order,OrderItem

# Create your models here.
ORDER_STATUS_CHOICES = (
	('unverified','Unverified'),
	('verified','Verified'),
	('dispatched','Dispatched'),
	('delivered','Delivered')
)

class Order(models.Model):
	user = models.ForeignKey(BasicUser,related_name='orders',on_delete=models.DO_NOTHING,null=True,blank=True)
	delivery_address = models.OneToOneField(Address,on_delete=models.DO_NOTHING,null=True,blank=True)
	is_cash_on_delivery = models.BooleanField(default=False,null=True,blank=True) 
	is_paid = models.BooleanField(default=False,null=True,blank=True)
	status = models.CharField(max_length=12,choices=ORDER_STATUS_CHOICES,null=True,blank=True)
	dispatch_date = models.DateTimeField(null=True,blank=True)
	delivered_date = models.DateTimeField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def total_cost(self):
		total = 0
		for item in self.items:
			total += item.get_cost()
		return total

class OrderItem(models.Model):
	order = models.ForeignKey(Order,related_name='items',on_delete=models.DO_NOTHING,null=True,blank=True)
	product = models.OneToOneField(Product,related_name='order_items',on_delete=models.DO_NOTHING,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_cost(self):
		return product.price*quantity
