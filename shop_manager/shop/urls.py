from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/<int:id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),  
    path('add/', views.add_product, name='add_product'), 
    path('cart/', views.cart_view, name='cart_view'),  
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), 


    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
