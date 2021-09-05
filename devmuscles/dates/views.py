from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    return JsonResponse({"response": "dates routes working"}, status=200)
