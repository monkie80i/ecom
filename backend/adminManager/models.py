from django.db import models
from tinymce import models as tinymce_models
# FAQCategory,FAQSubCategory,FAQ,BlogCategory,Blog,Testimonial
# Create your models here.
class FAQCategory(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	icon = models.URLField(max_length=1028,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

class FAQSubCategory(models.Model):
	faq_category = models.ForeignKey(FAQCategory,related_name="sub_category",on_delete=models.DO_NOTHING,null=True,blank=True)
	name = models.CharField(max_length=100,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	icon = models.URLField(max_length=1028,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

class FAQ(models.Model):
	question = models.CharField(null=True,blank=True,max_length=1048)
	answer = tinymce_models.HTMLField(null=True,blank=True)
	number_of_up_votes = models.IntegerField(null=True,default=0,blank=True)
	number_of_down_votes = models.IntegerField(null=True,default=0,blank=True)
	is_display_on_home_page = models.BooleanField(default=False)
	subcategory = models.ForeignKey(FAQSubCategory,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="faq")
	z_order = models.IntegerField(null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.question)

class BlogCategory(models.Model):
	
	name = models.CharField(null=False,max_length=50,blank=True)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

class Blog(models.Model):
	
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published')
		)
	title = models.CharField(null=True, max_length=100,blank=True)
	description = tinymce_models.HTMLField(null=True,blank=True)
	image = models.URLField(max_length=1028,null=True,blank=True)
	full_url = models.CharField(null=True,max_length=500,blank=True)
	blog_category = models.ForeignKey(BlogCategory,null=False,on_delete=models.DO_NOTHING,related_name='blogs',blank=True)
	status = models.CharField(max_length=500, default='draft', choices=STATUS_CHOICES,null=True,blank=True)
	reading_time = models.IntegerField(null=True, default=0,blank=True)
	is_display_on_home_page=models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)

class Testimonial(models.Model):
	
	customer_name = models.CharField(null=False, max_length=100,blank=True)
	customer_image = models.URLField(max_length=1028,null=True,blank=True)
	profession = models.CharField(null=False, max_length=100,blank=True)
	description = tinymce_models.HTMLField(null=True,blank=True)
	is_display_on_home_page = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.customer_name)