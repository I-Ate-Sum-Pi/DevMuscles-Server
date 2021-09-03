from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Workout


# Create your tests here.

class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.poodle_breed = Workout.objects.create(name='Poodle')
        self.dog = Dog.objects.create(name='Fido', breed=self.poodle_breed)
        self.user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')