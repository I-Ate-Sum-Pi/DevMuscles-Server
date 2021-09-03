from django.db import models

# Create your models here.
class user(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=500)

class workout(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    user_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)

class exercise(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits = 4, decimal_places=1)

class date(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.CharField(max_length=300)
    user_id = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)

