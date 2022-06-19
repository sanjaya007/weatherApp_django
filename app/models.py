from django.db import models

# Create your models here.
class Weather(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    status = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    wind_speed = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.place
    