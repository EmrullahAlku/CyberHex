from django.urls import path
from . import views

app_name = 'discussion_forum'

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('home/', views.forum_home, name='forum_home'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
