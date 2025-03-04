from django.contrib import admin
from .models import Category, Product, Review, Cart, CartItem, Order, OrderItem, Payment, Notification, Wishlist, SearchHistory, SellerAnnouncement

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(Wishlist)
admin.site.register(SearchHistory)
admin.site.register(SellerAnnouncement)
