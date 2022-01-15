from rest_framework import status,viewsets,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
import json
from userManager.permissions import IsOwner
from .models import Order,OrderItem
from . serializers import OrderSerializer,OrderItemSerilizer
# Create your views here.


class OrderViewset(viewsets.ViewSet):
	permission_classes = (IsOwner,permissions.IsAuthenticated)

	def list(self,request):
		user = request.user.basicuser
		orders = user.orders.all().filter(is_deleted=False)
		serializer = OrderSerializer(orders,many=True)
		return Response(serializer.data)

	def retrieve(self,request,pk=None):
		order = Order.objects.get(pk=pk)
		if order.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = OrderSerializer(order)
		return Response(serializer.data)

	def update(self,request,pk=None):
		order = Order.objects.get(pk=pk)
		if order.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = OrderSerializer(instance=order,data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	def destroy(self,request,pk=None):
		order = Order.objects.get(pk=pk)
		if order.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		order.is_active = False
		order.is_deleted = True
		order.save()
		return Response({'message':'deleted'})