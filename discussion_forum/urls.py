from django.urls import path
from . import views

app_name = 'discussion_forum'

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('home/', views.forum_home, name='forum_home'),
    path('topic/<str:topic_title>/', views.topic_detail, name='topic_detail'),
]
