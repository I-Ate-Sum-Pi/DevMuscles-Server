from django.http import Http404
from rest_framework.views import APIView
from .models import Date
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import DateSerializer
from rest_framework.decorators import api_view

# Create your views here.

class DateList(APIView):
    def get(self, request, user_id, format=None):
            dates = Date.objects.filter(user_id__pk = user_id)
            serializer = DateSerializer(dates, many=True)
            return Response(serializer.data)

    def post(self, request, user_id, format=None):
        serializer = DateSerializer(data=request.data)
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
        date = self.get_object(user_id, date_id)
        serializer = DateSerializer(date)
        return Response(serializer.data)

    def put(self, request, user_id, date_id, format=None):
        date = self.get_object(user_id, date_id)
        serializer = DateSerializer(date, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, date_id, format=None):
        workout = self.get_object(user_id, date_id)
        workout.delete()
        return Response("Date has successfully been deleted", status=status.HTTP_204_NO_CONTENT)    

                   

