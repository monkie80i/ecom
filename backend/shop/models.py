from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	isActive = models.BooleanField(default=True)
	isDeleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Product(models.Model):
	category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	#images
	description = models.TextField(null=True,blank=True)
	price = models.FloatField(null=True,blank=True)
	stock = models.IntegerField(null=True,blank=True)
	isActive = models.BooleanField(default=True)
	isDeleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
