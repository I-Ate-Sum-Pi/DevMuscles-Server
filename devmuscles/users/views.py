from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, UserSerializer

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():   
            account = serializer.save()
            token = Token.objects.get(user=account)
            data['username'] = account.username
            data['token'] = token.key
            data['id'] = token.user_id
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        if str(request.user) != str(serializer.data['username']):
            return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.data)

    #if user changes username this breaks, need to be able to update email and password:
    # def put(self, request, user_id, format=None):
    #     user = self.get_object(user_id)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         print(request.user)
    #         print(serializer.validated_data['username'])
    #         if str(request.user) != str(serializer.validated_data['username']):
    #             return Response("You are unauthorized to access this", status = status.HTTP_401_UNAUTHORIZED)
    #         else:
    #             serializer.save()
    #             return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        if str(request.user) != str(serializer.data['username']):
            return Response("You are unauthorized to delete this", status = status.HTTP_401_UNAUTHORIZED)
        else:    
            user.delete()
            return Response("User has been successfully deleted", status=status.HTTP_204_NO_CONTENT)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

