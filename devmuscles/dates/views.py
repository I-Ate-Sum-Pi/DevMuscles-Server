from django.http import Http404
from rest_framework.views import APIView
from .models import Date
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import DateSerializer
from workouts.serializers import WorkoutSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from workouts.models import Workout
from uuid import uuid4



# Create your views here.

class DateList(APIView):
    def get(self, request, user_id, format=None):
        query = request.GET.get('date')
        if query != None:
            dates = Date.objects.filter(user_id__pk = user_id).filter(date=query)
            date_serializer = DateSerializer(dates, many=True)
            workout_data = []
            for i in range(len(date_serializer.data)):
                workout = Workout.objects.filter(user_id__pk = user_id).get(id = date_serializer.data[i]['workout_id'])
                workout_serializer = WorkoutSerializer(workout)
                workout_data.append(workout_serializer.data)
            return Response({"dates": date_serializer.data, "workouts": workout_data})
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        dates = Date.objects.filter(user_id__pk = user_id)
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data)

    def post(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to post this here", status = status.HTTP_401_UNAUTHORIZED)
        new_uuid = uuid4()
        new_data = {"id": str(new_uuid), "workout_id": request.data['workout_id'], "user_id": user_id, "date": request.data['date'], "time": request.data['time'], "completed": request.data['completed']}
        serializer = DateSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class DateDetail(APIView):
    def get_object(self, user_id, date_id):
        try:
            return Date.objects.filter(user_id__pk=user_id).get(id = date_id)
        except Date.DoesNotExist:
            raise Http404  

    def get(self, request, user_id, date_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        date = self.get_object(user_id, date_id)
        date_serializer = DateSerializer(date)
        workout = Workout.objects.filter(user_id__pk = user_id).get(id = date_serializer.data['workout_id'])
        workout_serializer = WorkoutSerializer(workout)
        return Response({"date": date_serializer.data, "workout": workout_serializer.data })

    def put(self, request, user_id, date_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to post this here", status = status.HTTP_401_UNAUTHORIZED)
        date = self.get_object(user_id, date_id)
        new_data = {"id": date_id, "workout_id": request.data['workout_id'], "user_id": user_id, "date": request.data['date'], "time": request.data['time'], "completed": request.data['completed']}
        serializer = DateSerializer(date, new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, date_id, format=None):
        user = User.objects.get(pk=user_id)
        if request.user != user:
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        workout = self.get_object(user_id, date_id)
        workout.delete()
        return Response("Date has successfully been deleted", status=status.HTTP_204_NO_CONTENT)    

                   

