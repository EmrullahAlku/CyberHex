from django.urls import include, path
from . import views

app_name = 'user_accounts'

urlpatterns = [
    path('', views.accounts_index, name='accounts_index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]
