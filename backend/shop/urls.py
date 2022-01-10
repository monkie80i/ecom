from django.urls import path
from .views import CategoryViewset,ProductViewset,list_products_of_category,WishListItemViewset,wishlist_retrieve,wishlist_empty
from .views import CartItemViewset,cart_retrieve,cart_empty,cart_checkout

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
	path('wish-list/item',WishListItemViewset.as_view({
		'post':'create'
	})),
	path('wish-list/item<str:pk>',WishListItemViewset.as_view({
		'put':'partial_update',
		'delete':'destroy'
	})),
	path('wish-list',wishlist_retrieve),
	path('wish-list/empty',wishlist_empty),
	path('cart/item',CartItemViewset.as_view({
		'post':'create'
	})),
	path('cart/item<str:pk>',CartItemViewset.as_view({
		'put':'partial_update',
		'delete':'destroy'
	})),
	path('cart',cart_retrieve),
	path('cart/empty',cart_empty),
	path('cart/checkout',cart_checkout)

]