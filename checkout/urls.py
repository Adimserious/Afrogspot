from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/',
         views.order_confirmation,
         name='order_confirmation'),
    path('order-email-confirmation/<int:order>/',
         views.send_order_confirmation_email,
         name='order_email-confirmation'),
    path('order-history/', views.order_history, name='order_history'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('payment/execute/', views.execute_payment, name='execute_payment'),
    path('payment/cancel/', views.cancel_payment, name='cancel_payment'),
]
