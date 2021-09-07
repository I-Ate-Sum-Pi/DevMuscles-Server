from exercises.views import ExerciseList, ExerciseDetail
from dates.views import DateList, DateDetail
from workouts.views import WorkoutList, WorkoutDetail
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:user_id>', UserDetail.as_view()),
    path('<int:user_id>/workouts', WorkoutList.as_view()),
    path('<int:user_id>/workouts/<str:workout_id>', WorkoutDetail.as_view()),
    path('<int:user_id>/workouts/<str:workout_id>/exercises', ExerciseList.as_view()),
    path('<int:user_id>/workouts/<str:workout_id>/exercises/<str:exercise_id>', ExerciseDetail.as_view()),
    path('<int:user_id>/dates', DateList.as_view()),
    path('<int:user_id>/dates/<str:date_id>', DateDetail.as_view()),    
]