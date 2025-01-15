from . import views
from django.urls import path

urlpatterns = [
    # path('', views.TopicList.as_view(), name='feed'),
    path('', views.my_feed, name='feed'),
]