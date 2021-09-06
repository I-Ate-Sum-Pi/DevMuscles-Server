from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User


# Create your tests here.

class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username = 'test', email='myemail@crazymail.com', password='mypassword')

class TestWorkoutViews(BaseTestCase):
    c = Client()

    def test_status_code_is_200(self):
        response = self.c.get(f'/users/{self.user.id}')
        data = response.json()
        print(response)
        print(data)
        assert response.status_code == 200


            