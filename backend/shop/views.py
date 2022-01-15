from rest_framework import status,viewsets,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Category,Product,Wishlist,WishListItem,Cart,CartItem,ProductReview
from .serializers import CategorySerializer,ProductSerializer,WishListItemSerializer
from .serializers import WishListSerializer,CartItemSerializer,CartSerializer,ProductReviewSerializer
from .serializers import ConfirmOrderSerializer
import json

from userManager.permissions import IsOwner
from userManager.serializers import AddressSerializer
from django.views.decorators.csrf import csrf_exempt
from order.models import Order,OrderItem
from order.serializers import OrderSerializer,OrderItemSerilizer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CategoryViewset(viewsets.ViewSet):

	def list(self,request):
		categories = Category.objects.all().filter(is_active=True)
		serializer = CategorySerializer(categories,many=True)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=CategorySerializer)
	def create(self,request):
		serializer = CategorySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_201_CREATED)


	def retrieve(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CategorySerializer(category)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=CategorySerializer)
	def update(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CategorySerializer(instance=category,data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	@swagger_auto_schema(request_body=CategorySerializer)
	def partial_update(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CategorySerializer(instance=category,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		category.is_active = False
		category.is_deleted = True
		category.save()
		return Response({'message':'deleted'})

class ProductViewset(viewsets.ViewSet):

	def list(self,request):
		products = Product.objects.all().filter(is_active=True)
		serializer = ProductSerializer(products,many=True)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=ProductSerializer)
	def create(self,request):
		serializer = ProductSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_201_CREATED)


	def retrieve(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=ProductSerializer)
	def update(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(instance=product,data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	@swagger_auto_schema(request_body=ProductSerializer)
	def partial_update(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(instance=product,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		product.is_active = False
		product.is_deleted = True
		product.save()
		return Response({'message':'deleted'})

@api_view(['GET'])
def list_products_of_category(request,name=None):
	category = Category.objects.get(name=name)
	products = category.products.all().filter(is_active=True)
	serializer = ProductSerializer(products,many=True)
	return Response(serializer.data)

class WishListItemViewset(viewsets.ViewSet):
	permission_classes = (IsOwner,permissions.IsAuthenticated)

	@swagger_auto_schema(request_body=WishListItemSerializer)
	def create(self,request):
		serializer = WishListItemSerializer(
			data=request.data,
			context={'wish_list':request.user.basicuser.wishlist}
		)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_201_CREATED)
	
	@swagger_auto_schema(request_body=WishListItemSerializer)
	def partial_update(self,request,pk=None):
		item = WishListItem.objects.get(pk=pk)
		if item.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = WishListItemSerializer(instance=item,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		item = WishListItem.objects.get(pk=pk)
		if item.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		item.is_active = False
		item.is_deleted = True
		item.save()
		return Response({'message':'deleted'})

@api_view(['GET'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def wishlist_retrieve(request):
	wish_list = request.user.basicuser.wishlist
	if wish_list.is_deleted:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = WishListSerializer(wish_list)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def wishlist_empty(request):
	"""
	Removes all items froma a wishlist
	"""
	wish_list = request.user.basicuser.wishlist
	if wish_list.is_deleted:
		return Response(status=status.HTTP_404_NOT_FOUND)
	items = wish_list.items.all().filter(is_deleted=False)
	for item in items:
		item.is_active = False
		item.is_deleted = True
		item.save()
	serializer = WishListSerializer(wishlist)
	return Response(serializer.data)


class CartItemViewset(viewsets.ViewSet):
	permission_classes = (IsOwner,permissions.IsAuthenticated)

	@swagger_auto_schema(request_body=CartItemSerializer)
	def create(self,request):
		serializer = CartItemSerializer(
			data=request.data,
			context={'cart':request.user.basicuser.cart}
		)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_201_CREATED)
	
	@swagger_auto_schema(request_body=CartItemSerializer)
	def partial_update(self,request,pk=None):
		item = CartItem.objects.get(pk=pk)
		if item.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CartItemSerializer(instance=item,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		item = CartItem.objects.get(pk=pk)
		if item.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		item.is_active = False
		item.is_deleted = True
		item.save()
		return Response({'message':'deleted'})

@api_view(['GET'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def cart_retrieve(request):
	cart = request.user.basicuser.cart
	if cart.is_deleted:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = CartSerializer(cart)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def cart_empty(request):
	"""
	Removes all items froma a wishlist
	"""
	cart = request.user.basicuser.cart
	if cart.is_deleted:
		return Response(status=status.HTTP_404_NOT_FOUND)
	items = cart.items.all().filter(is_deleted=False)
	for item in items:
		item.is_active = False
		item.is_deleted = True
		item.save()
	serializer = CartSerializer(wishlist)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def cart_checkout(request):
	"""create an unconfirmed order
		retun possible delivery addresses
		send otp
	"""
	user = request.user.basicuser
	cart = user.cart
	print(cart.items.all().filter(is_deleted=False))
	if cart.is_empty():
		message ={
			"detail":"The cart is empty."
		}
		return Response(message)
	order = Order(
		user=user,
		status ='unverified'
	)
	order.save()
	for cart_item in cart.items.all():
		order_item = OrderItem(
			order = order,
			product = cart_item.product,
			quantity = cart_item.quantity
		)
		order_item.save()
	cart.clear()	
	#send otp
	address = request.user.basicuser.addresses.all().filter(is_deleted=False)
	addresses = AddressSerializer(address,many=True)
	output = {}
	output['addresses'] = addresses.data
	output["order_id"] = order.id
	return Response(output,status=status.HTTP_201_CREATED)

@swagger_auto_schema(method='post',request_body=ConfirmOrderSerializer)
@api_view(['POST'])
@permission_classes([IsOwner,permissions.IsAuthenticated])
def confirm_order(request):
	"""
	with the list of products
	"""
	serializer = ConfirmOrderSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	conf = serializer.save()
	output = conf.confirm()
	return Response(output)

