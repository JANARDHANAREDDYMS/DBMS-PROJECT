from django.db import models
from django.db import connection

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.id}:{self.city} ({self.code})'


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        to_field='code',
        on_delete=models.CASCADE,
        related_name='departures',
    )
    destination = models.ForeignKey(
        Airport,
        to_field='code',
        on_delete=models.CASCADE,
        related_name='arrivals',
    )
    duration = models.IntegerField(null=True,blank=True)
    arrival = models.CharField(null=True,max_length=64)
    departure = models.CharField(null=True,max_length=64)

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}'


class Passenger(models.Model):
    id = models.BigAutoField(unique=True,primary_key=True,verbose_name='ID')
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField(null=True,)
    flights = models.ManyToManyField(Flight, blank = True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"