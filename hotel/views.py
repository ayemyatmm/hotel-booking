from django.shortcuts import render
from django.views import generic

from .models import Room, Booking, RoomService

# Create your views here.
def index(request):
    return render(request, 'index.html')

class RoomListView(generic.ListView):
    model = Room
    paginate_by = 10
    fields = '__all__'

class RoomDetailView(generic.DetailView):
    model = Room

class BookingListView(generic.ListView):
    model = Booking

class BookingDetailView(generic.DetailView):
    model = Booking
    