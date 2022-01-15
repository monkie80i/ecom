from rest_framework import serializers
from .models import Category,Product,Wishlist,WishListItem,Cart,CartItem,ProductReview

#from shop.serializers import CategorySerializer,ProductSerializer,WishListItemSerializer,WishListSerializer,CartItemSerializer,CartSerializer,ProductReviewSerializer

# Create your serializers here.

class NonDetletedListSerializer(serializers.ListSerializer):
	
	def to_representation(self, data):
		data = data.filter(is_deleted=False)
		return super(NonDetletedListSerializer, self).to_representation(data)

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		list_serializer_class = NonDetletedListSerializer
		fields = ['id','name','created']

class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=True,read_only=True)
	category_set = serializers.ListField(
		child=serializers.IntegerField(),allow_empty=True,write_only=True
	)

	class Meta:
		model = Product
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'category',
			'name',
			'description',
			'price',
			'stock',
			'category_set',
			'created'
		]

	def create(self,validated_data):
		print(validated_data)
		categories = validated_data.pop('category_set')
		product = Product.objects.create(**validated_data)
		for cat in categories:
			try:
				product.category.add(Category.objects.get(id=cat))
			except:
				pass
		return product

class WishListItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = WishListItem
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'product',
			'quantity',
			'created'
		]



class WishListSerializer(serializers.ModelSerializer):
	items = WishListItemSerializer(many=True)

	class Meta:
		model = Wishlist
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'user',
			'items',
			'created'
		]

class CartItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer()
	class Meta:
		model = CartItem
		list_serializer_class = NonDetletedListSerializer
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
		model = Cart
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'user',
			'items',
			'created'
		]

class ProductReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductReview
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'user',
			'product',
			'ratings',
			'comment',
			'created'
		]
