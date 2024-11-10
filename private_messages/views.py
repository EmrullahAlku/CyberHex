from django.shortcuts import render
from .models import Message

def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'private_messages/inbox.html', {'messages': messages})

def messages_index(request):
    return render(request, 'private_messages/messages_index.html')
