from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profile_view, name='profile_view'),
]
