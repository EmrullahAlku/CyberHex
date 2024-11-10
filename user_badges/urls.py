from django.urls import path
from . import views

app_name = 'user_badges'

urlpatterns = [
    path('', views.badges_index, name='badges_index'),
    path('badges/', views.badge_list, name='badge_list'),
]
