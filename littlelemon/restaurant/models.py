from django.db import models

class Booking(models.Model):

    name = models.CharField(max_length=255)
    NumGuest = models.SmallIntegerField()
    BookingDate = models.DateTimeField()


class Menu(models.Model):
   
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    #add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
