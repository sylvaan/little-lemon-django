from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    image = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} (Slot: {self.reservation_slot})"

