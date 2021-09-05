from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList

urlpatterns = [
    path('', UserList.as_view(), name='all-users'),
]