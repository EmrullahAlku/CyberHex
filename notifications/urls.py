from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notifications_index, name='notifications_index'),
    path('notifications/', views.notification_list, name='notification_list'),
]
