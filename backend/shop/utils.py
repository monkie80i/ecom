from shop.models import Category,Product,Wishlist,WishListItems,Cart,CartItems,ProductReview

def wish_list_has_product(wish_list=wish_list,product=product):
	return wish_list.items.all().filter(product=product).exists()
