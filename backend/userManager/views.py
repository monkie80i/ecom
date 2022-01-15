from django.shortcuts import render
from rest_framework import status,viewsets,permissions
from rest_framework.response import Response
from userManager.permissions import IsOwner
from .models import BasicUser,Address
from .serializers import AddressSerializer,BasicUserSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class UserAddressViewset(viewsets.ViewSet):
	permission_classes = (IsOwner,permissions.IsAuthenticated)

	def list(self,request):
		"""
		lists the address of user
		"""
		address = request.user.basicuser.addresses.all().filter(is_deleted=False)
		serializer = AddressSerializer(address,many=True)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=AddressSerializer)
	def create(self,request):
		basic_user = request.user.basicuser
		serializer = AddressSerializer(data=request.data,context={'user':basic_user})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_201_CREATED)


	def retrieve(self,request,pk=None):
		address = Address.objects.get(pk=pk)
		if address.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = AddressSerializer(address)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=AddressSerializer)
	def update(self,request,pk=None):
		address = Address.objects.get(pk=pk)
		if address.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = AddressSerializer(instance=address,data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	

	@swagger_auto_schema(request_body=AddressSerializer)
	def partial_update(self,request,pk=None):
		address = Address.objects.get(pk=pk)
		if address.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = AddressSerializer(instance=address,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

	def destroy(self,request,pk=None):
		address = Address.objects.get(pk=pk)
		if address.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		address.is_active = False
		address.is_deleted = True
		address.save()
		return Response({'message':'deleted'})



class ProfileViewset(viewsets.ViewSet):
	permission_classes = (IsOwner,permissions.IsAuthenticated)

	def retrieve(self,request):
		basic_user = request.user.basicuser
		if basic_user.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = BasicUserSerializer(basic_user)
		return Response(serializer.data)

	@swagger_auto_schema(request_body=BasicUserSerializer)
	def partial_update(self,request,pk=None):
		basic_user = request.user.basicuser
		if basic_user.is_deleted:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = BasicUserSerializer(instance=basic_user,data=request.data,partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data,status=status.HTTP_202_ACCEPTED)	
