from django.db import models

# Create your models here.

class Exercise(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits = 4, decimal_places=1)