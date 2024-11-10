from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='messages_index'),
    path('inbox/', views.inbox, name='inbox'),
]
