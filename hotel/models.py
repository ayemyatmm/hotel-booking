from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    """ロンム"""
    name = models.CharField(max_length=100)
    price = models.TextField(max_length=100)
    description = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to='images/',default='defo')

    class Meta:
        ordering = ["name", "price","description"]

    def get_absolute_url(self):
        return reverse('room-detail',args=[str(self.id)])

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    arrival_date = models.DateField(null=True, blank=True)
    deperture_date = models.DateField(null=True, blank=True)
    number_rooms = models.CharField(max_length=2)
    guest = models.CharField(max_length=2)
    room = models.ForeignKey(Room,on_delete= models.CASCADE)

    def __str__(self):
        return str(self.name)

class RoomService(models.Model):
    swimming_pool = models.BooleanField(blank=True)
    baby_bed = models.BooleanField(blank=True)
    convience_store = models.BooleanField(blank=True)
    booking = models.ForeignKey(Booking,on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return str(self.swimming_pool)

class Restaurants(models.Model):
    photo = models.ImageField(upload_to='images/',default='defo')

    def __str__(self):
        return self.photo