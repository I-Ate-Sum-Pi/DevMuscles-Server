from exercises.views import ExerciseList, ExerciseDetail
from dates.views import DateList, DateDetail
from workouts.views import userWorkouts, userWorkout
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:user_id>', UserDetail.as_view()),
    path('<int:user_id>/workouts', userWorkouts),
    path('<int:user_id>/workouts/<int:workout_id>', userWorkout),
    path('<int:user_id>/workouts/<int:workout_id>/exercises', ExerciseList.as_view()),
    path('<int:user_id>/workouts/<int:workout_id>/exercises/<int:exercise_id>', ExerciseDetail.as_view()),
    path('<int:user_id>/dates', DateList.as_view()),
    path('<int:user_id>/dates/<int:date_id>', DateDetail.as_view()),


    
]