from django.db import models
from django.utils import timezone
# import datetime 

# Create your models here.
class Date(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.CharField(max_length=300)
    user_id = models.CharField(max_length=500)
    date = models.DateField(max_length=10)
    time = models.IntegerField(default=1000)
    completed = models.BooleanField(default=False)