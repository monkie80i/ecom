from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# BasicUser,Address
# Create your models here.
class BasicUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,blank=True)
	phone = PhoneNumberField(null=True,blank=True)
	photo = models.URLField(max_length=1028,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Address(models.Model):
	user = models.ForeignKey(BasicUser,related_name='addresses',on_delete=models.DO_NOTHING,null=True,blank=True)
	line_1 = models.CharField(max_length=100,null=True,blank=True)
	line_2 = models.CharField(max_length=100,null=True,blank=True)
	city = models.CharField(max_length=50,null=True,blank=True)
	state = models.CharField(max_length=50,null=True,blank=True)
	country = models.CharField(max_length=50,null=True,blank=True)
	pincode = models.CharField(max_length=50,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)