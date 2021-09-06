from django import http
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Exercise
from .serializers import ExerciseSerializer

# Create your views here.

class ExerciseList(APIView):
    def get(self, request, user_id, workout_id, format=None):
        exercises = Exercise.objects.filter(workout_id__id=workout_id)
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    def post(self, request, user_id, workout_id, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ExerciseDetail(APIView):
    pass