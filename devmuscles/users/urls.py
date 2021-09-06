from workouts.views import userWorkouts
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:user_id>', UserDetail.as_view()),
    path('<int:user_id>/workouts', userWorkouts)
]