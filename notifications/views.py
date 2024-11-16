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
    # Continue with like logic...
    return JsonResponse({'status': 'liked'})

def comment_post(request, post_id):
    post = Post.objects.get(id=post_id)
    create_comment_notification(post.user, post)  # Notify post owner
    # Continue with comment logic...
    return JsonResponse({'status': 'commented'})


def notification_list(request):
    # Retrieve unread notifications for the logged-in user
    notifications = Notification.objects.filter(user=request.user, read=False)
    
    # If the user is viewing the page, mark notifications as read
    if request.method == "GET":
        notifications.update(read=True)  # Mark all notifications as read when the user accesses them

    return render(request, 'notifications/notification_list.html', {'notifications': notifications})
