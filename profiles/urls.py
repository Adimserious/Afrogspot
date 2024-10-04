from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profile_view, name='profile_view'),
    path('delete/', views.profile_delete, name='profile_delete'),
    path('profile/create/', views.create_profile, name='create_profile'),
]
