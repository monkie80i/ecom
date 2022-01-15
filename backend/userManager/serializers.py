from rest_framework import serializers
from .models import BasicUser,Address
from shop.models import Wishlist,Cart
from dj_rest_auth.registration.serializers import RegisterSerializer

#from userManager.serializers import BasicUserSerializer,AddressSerializer

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

	def create(self,validated_data):
		address = Address.objects.create(**validated_data)
		user = self.context.get('user')
		address.user = user
		address.save()
		return address

class CustomRegisterSerializer(RegisterSerializer):
	def custom_signup(self, request, user):
		basic_user = BasicUser(user=user)
		basic_user.save()
		wish_list = Wishlist(user=basic_user)
		wish_list.save()
		cart = Cart(user=basic_user)
		cart.save()