from django.urls import path
from .views import ProfileViewset,UserAddressViewset

urlpatterns = [
	# User address endpoints
	path('user/address',UserAddressViewset.as_view({
		'get':'list',
		'post':'create'
	})),
	path('user/address/<int:pk>',UserAddressViewset.as_view({
		'get':'retrieve',
		'post':'update',
		'put':'partial_update',
		'delete':'destroy'
	})),
	# Profile Endpoints
	path('user/profile',ProfileViewset.as_view({
		'get':'retrieve',
		'put':'partial_update',
	})),
]