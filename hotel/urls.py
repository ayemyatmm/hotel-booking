from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.RoomListView.as_view(), name= "room"),
    path('room/<int:pk>', views.RoomDetailView.as_view(), name = 'room-detail'),
    path('room/<int:pk>/booking_create/', views.BookingCreate.as_view(),name = 'booking-create'),
    path('restaurants/',views.RestaurantsView.as_view(),name='restaurants'),
    path('room/<int:pk>/booking_list', views.BookingListView.as_view(), name = 'booking'),
    path('room/booking-detail/<int:pk>', views.BookingDetailView.as_view(), name = 'booking-detail'),
    path('room/booking-detail/<int:pk>/service/',views.RoomServiceView.as_view(),name='add-service'),
]

   
