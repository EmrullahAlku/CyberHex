from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]
