from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Product,Wishlist,WishListItem,Cart,CartItem,ProductReview
from .serializers import CategorySerializer,ProductSerializer,WishListItemSerializer
from .serializers import WishListSerializer,CartItemSerializer,CartSerializer,ProductReviewSerializer
import json

# Create your views here.

class CategoryViewset(viewsets.ViewSet):
	def list(self,request):
		categories = Category.objects.all().filter(is_active=True)
		serializer = CategorySerializer(categories,many=True)
		return Response(serializer.data)

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

	def update(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CategorySerializer(instance=category,data=request.data)
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	def partial_update(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = CategorySerializer(instance=category,data=request.data,partial=True)
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		category = Category.objects.get(pk=pk)
		if category.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		category.is_active = False
		category.is_deleted = True
		return Response({'message':'deleted'})

class ProductViewset(viewsets.ViewSet):

	def list(self,request):
		products = Product.objects.all().filter(is_active=True)
		serializer = ProductSerializer(products,many=True)
		return Response(serializer.data)

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

	def update(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(instance=product,data=request.data)
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	def partial_update(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(instance=product,data=request.data,partial=True)
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		product = Product.objects.get(pk=pk)
		if product.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		product.is_active = False
		product.is_deleted = True
		return Response({'message':'deleted'})

@api_view(['GET'])
def list_products_of_category(request,name=None):
	category = Category.objects.get(name=name)
	products = category.products.all().filter(is_active=True)
	serializer = ProductSerializer(products,many=True)
	return Response(serializer.data)

