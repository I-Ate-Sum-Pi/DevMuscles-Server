from django.http import Http404
from rest_framework.views import APIView
from .models import Workout
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import WorkoutSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from uuid import uuid4

# Create your views here.
class WorkoutList(APIView):   
    from rest_framework.authentication import TokenAuthentication
    from rest_framework.permissions import IsAuthenticated 
    def get(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        workouts = Workout.objects.filter(user_id__pk = user_id)
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    

    def post(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to post this here", status = status.HTTP_401_UNAUTHORIZED) 
        new_uuid = uuid4()
        new_data = {"id": str(new_uuid), "name": request.data['name'], "user_id": user_id}
        serializer = WorkoutSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    def get_object(self, user_id, workout_id):
        try:
            return Workout.objects.filter(user_id__pk = user_id).get(id = workout_id)
        except Workout.DoesNotExist:
            raise Http404

    def get(self, request, user_id, workout_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED) 
        workout = self.get_object(user_id, workout_id)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)


    def put(self, request, user_id, workout_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        workout = self.get_object(user_id, workout_id)
        new_data = {"id": workout_id, "name": request.data['name'], "user_id": user_id}
        serializer = WorkoutSerializer(workout, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, workout_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        workout = self.get_object(user_id, workout_id)
        workout.delete()
        return Response("Workout has successfully been deleted", status=status.HTTP_204_NO_CONTENT)
        

   