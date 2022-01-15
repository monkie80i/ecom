from django.urls import path
from .views import OrderViewset
urlpatterns = [
	path('user/order',OrderViewset.as_view({
		'get':'list'
	})),
	path('user/order/<str:pk>',OrderViewset.as_view({
		'get':'retrieve',
		'put':'update',
		'delete':'destroy'
	})),
]