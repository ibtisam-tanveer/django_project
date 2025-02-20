from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need origin country destination night price
    origin_country = models.CharField(max_length=50)
    destination_country = models.CharField(max_length=50)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()