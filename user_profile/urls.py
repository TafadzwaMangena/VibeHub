from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_profile, name='profile'),
]