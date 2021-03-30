from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.RoomListView.as_view(), name= "room"),
    path('room/<int:pk>', views.RoomDetailView.as_view(), name = 'room-detail'),
    path('booking/', views.BookingListView.as_view(), name = 'booking'),
    path('booking/<int:pk>', views.BookingDetailView.as_view(), name = 'booking-detail'),
]
