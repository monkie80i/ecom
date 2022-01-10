from rest_framework import serializers
from .models import Category,Product,Wishlist,WishListItems,Cart,CartItems,ProductReview

# Create your serializers here.
class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name','created']

class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=True)
	class Meta:
		model = Product
		fields = [
			'id',
			'category',
			'name',
			'description',
			'price',
			'stock',
			'created'
		]

class WishListItemsSerializer(serializers.ModelSerializer):
	product = ProductSerializer()
	class Meta:
		model = WishListItems
		fields = [
			'id',
			'product',
			'quantity',
			'created'
		]

class WishListSerializer(serializers.ModelSerializer):
	items = WishListItemsSerializer(
		many=True
		)

	class Meta:
		model = Wishlist
		fields = [
			'id',
			'user',
			'items',
			'created'
		]


class CartItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer()
	class Meta:
		model = WishListItems
		fields = [
			'id',
			'product',
			'quantity',
			'created'
		]

class CartSerializer(serializers.ModelSerializer):
	items = CartItemSerializer(
		many=True
		)

	class Meta:
		model = Wishlist
		fields = [
			'id',
			'user',
			'items',
			'created'
		]

class ProductReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductReview
		fields = [
			'id',
			'user',
			'product',
			'ratings',
			'comment',
			'created'
		]
