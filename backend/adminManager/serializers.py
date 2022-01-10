from rest_framework import serializers
from .models import FAQCategory,FAQSubCategory,FAQ,BlogCategory,Blog,Testimonial

class FAQCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQCategory
		fields = [
			'id',
			'name',
			'description',
			'icon',
			'created'
		]

class FAQSubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQSubCategory
		fields = [
			'id',
			'faq_category',
			'name',
			'description',
			'icon',
			'created'
		]

class FAQSerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQ
		fields = [
			'id',
			'question',
			'answer',
			'number_of_up_votes',
			'number_of_down_votes',
			'is_display_on_home_page',
			'subcategory',
			'z_order',
			'created'
		]

class BlogCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogCategory
		fields = [
			'id',
			'name',
			'created'
		]

class BlogSerializer(serializers.ModelSerializer):
	blog_category = BlogCategorySerializer(many=True)

	class Meta:
		model = Blog
		fields = [
			'id',
			'title',
			'description',
			'image',
			'full_url',
			'blog_category',
			'status',
			'reading_time',
			'is_display_on_home_page',
			'created'
		]
		
class TestimonialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Testimonial
		fields = [
			'id',
			'customer_name',
			'customer_image',
			'profession',
			'description',
			'is_display_on_home_page',
			'created'
		]