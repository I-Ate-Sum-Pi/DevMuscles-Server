from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from .models import Workout
# from rest_framework.test import APIRequestFactory

from .views import WorkoutList


# Create your tests here.

class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username = 'myusername', email='myemail@crazymail.com', password='mypassword')
        self.chest_workout = Workout.objects.create(id='TYEA', user_id=self.user, name='chest')

class TestWorkoutViews(BaseTestCase):
    factory = RequestFactory()
    c = Client()

    def test_home(self):
        response = self.c.get(f'/users/{self.user.id}/workouts')
        data = response.json()
        print(response)
        print(data)
        assert response.status_code == 200
        assert data[0]['name'] == 'chest'

    def test_workout_name_to_be_chest(self):
        response = self.c.get(f'/users/{self.user.id}/workouts')
        data = response.json()
        assert data[0]['name'] == 'chest'

    
