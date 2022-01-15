from rest_framework import serializers
from .models import Order,OrderItem
from userManager.serializers import AddressSerializer

#from order.serializers import OrderSerializer,OrderItemSerilizer

class OrderItemSerilizer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = [
			'id',
			'order',
			'product',
			'quantity',
			'created'
		]

class OrderSerializer(serializers.ModelSerializer):
	delivery_address = AddressSerializer()
	items = OrderItemSerilizer(many=True,read_only=True)

	class Meta:
		model = Order
		fields = [
			'id',
			'user',
			'items',
			'delivery_address',
			'is_cash_on_delivery',
			'is_paid',
			'status',
			'dispatch_date',
			'delivered_date',
			'total_cost',
			'created'
		]
		read_only_fields = ['id','user','delivery_address','total_cost','created']