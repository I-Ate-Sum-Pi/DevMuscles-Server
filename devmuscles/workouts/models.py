from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Workout(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500)



