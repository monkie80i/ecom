from django.urls import path
from .views import CategoryViewset,ProductViewset,list_products_of_category

urlpatterns = [
	path('category',CategoryViewset.as_view({
		'get':'list',
		'post':'create'
	})),
	path('category/<str:pk>',CategoryViewset.as_view({
		'get':'retrieve',
		'post':'update',
		'put':'partial_update',
		'delete':'destroy'
	})),
	path('product',ProductViewset.as_view({
		'get':'list',
		'post':'create'
	})),
	path('product/<str:pk>',ProductViewset.as_view({
		'get':'retrieve',
		'post':'update',
		'put':'partial_update',
		'delete':'destroy'
	})),
	path('product/category/<str:name>',list_products_of_category),
]