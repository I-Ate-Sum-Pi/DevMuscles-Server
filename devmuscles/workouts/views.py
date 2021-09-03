from django.shortcuts import render
from django.http import JsonResponse
from .models import Workout

# Create your views here.
def home(request):
    return JsonResponse({"something": "workout route working"}, status=200)