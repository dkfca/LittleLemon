from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
