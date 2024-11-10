from django.urls import path
from . import views

app_name = 'post_interactions'

urlpatterns = [
    path('', views.interactions_index, name='interactions_index'),
    path('post/<int:post_id>/comments/', views.post_comments, name='post_comments'),
]
