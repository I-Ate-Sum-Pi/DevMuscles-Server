from django.contrib import admin
from .models import date, exercise, user, workout
# Register your models here.
admin.site.register(workout)
admin.site.register(user)
admin.site.register(exercise)
admin.site.register(date)