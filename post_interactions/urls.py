from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='interactions_index'),
    path('post/<int:post_id>/comments/', views.post_comments, name='post_comments'),
]
