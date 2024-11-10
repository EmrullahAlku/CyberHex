from django.shortcuts import render
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.filter(user=request.user, read=False)
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def notifications_index(request):
    return render(request, 'notifications/notifications_index.html')
