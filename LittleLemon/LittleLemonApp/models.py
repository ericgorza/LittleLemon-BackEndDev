from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    guests = models.SmallIntegerField(default=6)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.name} : {str(self.price)}'
