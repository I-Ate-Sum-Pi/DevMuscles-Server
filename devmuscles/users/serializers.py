from rest_framework import serializers
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirmation')
        write_only_fields = ('password', 'password_confirmation')

    def create(self, validated_data):
        password=validated_data['password']
        password_confirmation=validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError({'password': 'Passwords must match.'}) 
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(password)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)