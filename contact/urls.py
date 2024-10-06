from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_message, name='send_message'),
    path('messages/', views.list_user_messages, name='list_user_messages'),
    path('messages/update/<int:message_id>/', views.update_message, name='update_message'),
    path('messages/delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('confirmation/', views.contact_confirmation, name='contact_confirmation'),
]
