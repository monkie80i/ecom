from rest_framework import serializers
from .models import BasicUser,Address

class BasicUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = BasicUser
		fields = [
			'id',
			'user',
			'phone',
			'photo',
			'created',
		]

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = [
			'id',
			'user',
			'line_1',
			'line_2',
			'city',
			'state',
			'country',
			'pincode',
			'created',
		]