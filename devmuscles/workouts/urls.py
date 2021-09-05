from django.urls import path
from .views import WorkoutList, WorkoutDetail, userWorkouts

urlpatterns = [
    path('', WorkoutList.as_view()),
    path('<int:workout_id>', WorkoutDetail.as_view()),
    path('user/<int:user_id>', userWorkouts, name="test")
]