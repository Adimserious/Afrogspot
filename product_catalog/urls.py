from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('manage/', views.manage_products, name='manage_products'),
    path('product/<int:product_id>/rate/', views.rate_product, name='rate_product'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
]