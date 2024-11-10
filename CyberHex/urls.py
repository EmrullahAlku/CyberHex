from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indeks, name='indeks'),
    path('accounts/', include('user_accounts.urls')),
    path('forum/', include('discussion_forum.urls')),
    path('messages/', include('private_messages.urls')),
    path('interactions/', include('post_interactions.urls')),
    path('notifications/', include('notifications.urls')),
    path('badges/', include('user_badges.urls')),
]
