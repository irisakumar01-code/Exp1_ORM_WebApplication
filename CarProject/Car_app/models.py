from django.db import models
from django.contrib import admin
# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price')
 