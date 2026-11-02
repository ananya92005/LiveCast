from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_room, name='create_room'),
    path('', views.list_rooms, name='list_rooms'),
    path('<int:room_id>/', views.room_detail, name='room_detail'),
    path('<int:room_id>/join/', views.join_room, name='join_room'),
    path('<int:room_id>/leave/', views.leave_room, name='leave_room'),
    path('<int:room_id>/messages/', views.room_messages, name='room_messages'),
]