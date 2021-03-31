from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Room, Booking, RoomService, Restaurants

# Create your views here.
def index(request):
    return render(request, 'index.html')

class RoomListView(generic.ListView):
    model = Room
    paginate_by = 10

class RoomDetailView(generic.DetailView):
    model = Room

class BookingCreate(generic.CreateView):
    model = Booking
    fields = ['name','arrival_date', 'deperture_date', 'number_rooms', 'guest','room']

    def get_success_url(self):
        return reverse('booking', kwargs={'pk': self.kwargs['pk'],})

    def get_initial(self):
        initial = super().get_initial()
      
        return initial

class RoomServiceView(generic.CreateView):
    model = RoomService
    fields = ['swimming_pool','baby_bed','convience_store','booking']

    def get_success_url(self):
        return reverse('booking-detail', kwargs={'pk': self.kwargs['pk'],})

class BookingUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Booking
    fields = '__all__'
    
class BookingDelete(LoginRequiredMixin,generic.DeleteView):
    model = Booking

class BookingListView(generic.ListView):
    model = Booking

class BookingDetailView(generic.DetailView):
    model = Booking
    
class RestaurantsView(generic.ListView):
    model = Restaurants