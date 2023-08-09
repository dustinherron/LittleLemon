from django.db import models

class Booking(models.Model):
    # id pk
    # Name
    # num guests
    # booking date
    # ! id is auto by django
    name = models.CharField(max_length=255)
    NumGuest = models.SmallIntegerField()
    BookingDate = models.DateTimeField()


class Menu(models.Model):
   
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
