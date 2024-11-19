from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from discussion_forum.models import Post
from user_accounts.models import User

def create_like_notification(user, post):
    message = f"Your post '{post.title}' was liked!"
    Notification.objects.create(user=user, message=message, notification_type='like', post=post)

def create_comment_notification(user, post):
    message = f"Your post '{post.title}' has a new comment!"
    Notification.objects.create(user=user, message=message, notification_type='comment', post=post)

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    create_like_notification(post.user, post) 
    
    return JsonResponse({'status': 'liked'})

def comment_post(request, post_id):
    post = Post.objects.get(id=post_id)
    create_comment_notification(post.user, post) 
    
    return JsonResponse({'status': 'commented'})

def notification_list(request):
    notifications = Notification.objects.filter(user=request.user, read=False)
    
    if request.method == "GET":
        notifications.update(read=True) 

    return render(request, 'notifications/notification_list.html', {'notifications': notifications})
