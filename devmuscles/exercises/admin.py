from django.contrib import admin
from rest_framework.views import exception_handler
from .models import Exercise
# Register your models here.
class ExerciseAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'reps', 'weight')

admin.site.register(Exercise, ExerciseAdmin)