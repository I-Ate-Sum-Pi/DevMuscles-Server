from django.db import models

# Create your models here.
class workout(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    user_id = models.CharField(max_length=300)
    name = models.CharField(max_length=500)



