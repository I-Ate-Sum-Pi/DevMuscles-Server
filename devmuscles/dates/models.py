from django.db import models

# Create your models here.
class date(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    workout_id = models.CharField(max_length=300)
    user_id = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)