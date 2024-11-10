from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='badges_index'),
    path('badges/', views.badge_list, name='badge_list'),
]
