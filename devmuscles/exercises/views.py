from django import http
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    return JsonResponse({"response":"exercies route working"}, status=200)
