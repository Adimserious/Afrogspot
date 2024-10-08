from django.urls import path
from . import views


urlpatterns = [
    path('cart/remove/<item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('cart/update/<item_id>/', views.update_cart_quantity,
         name='update_cart_quantity'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
