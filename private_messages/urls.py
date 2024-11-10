from django.urls import path
from . import views

app_name = 'private_messages'

urlpatterns = [
    path('', views.messages_index, name='messages_index'),
    path('inbox/', views.inbox, name='inbox'),
]
