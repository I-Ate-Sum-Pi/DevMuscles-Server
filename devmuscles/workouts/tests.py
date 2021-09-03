from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Workout


# Create your tests here.

class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
        self.chest_workout = Workout.objects.create(id='TYEA', user_id=self.user, name='chest')

class TestWorkoutViews(BaseTestCase):
    c = Client()

    def test_home(self):
        response = self.c.get(reverse('workout-home'))
        data = response.json()
        print(response)
        print(data)
        assert response.status_code == 200
        assert 'workout route working' in data['something']