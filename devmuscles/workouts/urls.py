from django.urls import path
from .views import WorkoutList, WorkoutDetail

urlpatterns = [
    path('', WorkoutList.as_view()),
    path('<int:workout_id>', WorkoutDetail.as_view()),
]