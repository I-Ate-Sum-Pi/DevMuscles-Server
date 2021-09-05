from django.contrib import admin
from .models import Workout
# Register your models here.
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name")

admin.site.register(Workout, WorkoutAdmin)

