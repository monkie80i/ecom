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
		read_only_fields = ['id','created']

	def create(self,validated_data):
		#print(validated_data)
		categories = validated_data.pop('category_set')
		product = Product.objects.create(**validated_data)
		for cat in categories:
			try:
				product.category.add(Category.objects.get(id=cat))
			except:
				pass
		return product

	def update(self, instance, validated_data):
		category_set = validated_data.pop('category_set')
		instance.name = validated_data.get('name',instance.name)
		instance.description = validated_data.get('description',instance.description)
		instance.price = validated_data.get('price',instance.price)
		instance.stock = validated_data.get('stock',instance.stock)
		categories = [ Category.objects.get(id=cat) for cat in category_set]
		instance.category.set(categories)
		instance.save()
		return instance

class ProductSerializerMinimal(serializers.ModelSerializer):
	#category = CategorySerializer(many=True,read_only=True)
	class Meta:
		model = Product
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'name',
			'price',
		]

class WishListItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False,read_only=True)
	product_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = WishListItem
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'product',
			'product_id',
			'quantity',
			'created'
		]

	def create(self,validated_data):
		product_id = validated_data.pop('product_id')
		product = Product.objects.get(id=product_id)
		wish_list = self.context.get("wish_list")
		if wish_list:
			if wish_list.items.all().filter(product=product).exists():
				raise Exception("Product already in wish list")
		wish_list_item = WishListItem.objects.create(**validated_data)
		if wish_list:
			wish_list_item.wish_list = wish_list
		wish_list_item.product = product
		wish_list_item.save()
		return wish_list_item
		

	def update(self, instance, validated_data):
		instance.quantity = validated_data.get('quantity',instance.quantity)
		instance.save()
		return instance


class WishListItemSerializerMinimal(serializers.ModelSerializer):
	product = ProductSerializerMinimal(many=False,read_only=True)
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
	items = WishListItemSerializerMinimal(many=True)
	class Meta:
		model = Wishlist
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'user',
			'items',
			'length',
			'created'
		]


class CartItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False,read_only=True)
	product_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = CartItem
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'product',
			'quantity',
			'product_id',
			'total_cost',
			'created'
		]
		read_only_fields = ['id','created','total_cost']

	def create(self,validated_data):
		product_id = validated_data.pop('product_id')
		product = Product.objects.get(id=product_id)
		cart = self.context.get("cart")
		if cart:
			if cart.items.all().filter(product=product).exists():
				raise Exception("Product already in cart")
		cart_item = CartItem.objects.create(**validated_data)
		if cart:
			cart_item.cart = cart
		cart_item.product = product
		cart_item.save()
		return cart_item
		

	def update(self, instance, validated_data):
		instance.quantity = validated_data.get('quantity',instance.quantity)
		instance.save()
		return instance

class CartItemSerializerMinimal(serializers.ModelSerializer):
	product = ProductSerializerMinimal(many=False,read_only=True)

	class Meta:
		model = CartItem
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'product',
			'quantity',
			'total_cost'
		]

class CartSerializer(serializers.ModelSerializer):
	items = CartItemSerializerMinimal(many=True)

	class Meta:
		model = Cart
		list_serializer_class = NonDetletedListSerializer
		fields = [
			'id',
			'user',
			'items',
			'length',
			'total_cost',
			'created'
		]
		read_only_fields = ['id','created','items','total_cost']

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
		read_only_fields = ['id','created']
