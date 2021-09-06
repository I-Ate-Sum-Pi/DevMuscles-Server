from django.contrib import admin
from .models import Date
# Register your models here.

class DateAdmin(admin.ModelAdmin):
    list_display=('id','workout_id', 'user_id', 'date', 'time', 'completed')

admin.site.register(Date, DateAdmin)
