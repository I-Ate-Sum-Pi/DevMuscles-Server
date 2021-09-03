from django.db import models

# Create your models here.
class users(models.Model):
    id = models.CharField(max_length=80)
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=500)

class workouts(models.Model):
    id = models.CharField(max_length=80)
    user_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)

class exercises(models.Model):
    id = models.CharField(max_length=80)
    workout_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits = 4, decimal_places=1)

class dates(models.Model):
    id = models.CharField(max_length=80)
    workout_id = models.CharField(max_length=300)
    user_id = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)

