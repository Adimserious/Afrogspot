from django.urls import path
from . import views
from .views import order_history

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order-email-confirmation/<int:order>/', views.send_order_confirmation_email, name='order_email-confirmation'),
    path('order-history/', views.order_history, name='order_history'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
