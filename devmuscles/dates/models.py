# from devmuscles.workouts.models import Workout
from django.contrib.auth.models import User
from django.db import models
from workouts.models import Workout
# import datetime 

# Create your models here.
class Date(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=10)
    time = models.IntegerField(default=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.id