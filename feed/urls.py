from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('', views.my_feed, name='feed'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/report/', views.report_post, name='report_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('topic/<int:topic_id>/', views.topic_posts, name='topic_posts'),
]