from django.shortcuts import render
from .models import Message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message

@login_required(login_url='login')
def inbox(request):
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-timestamp')
    
    return render(request, 'private_messages/inbox.html', {
        'messages': messages,
        'user': request.user
    })