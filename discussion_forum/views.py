from django.shortcuts import render, get_object_or_404
from .models import Topic

def forum_home(request):
    topics = Topic.objects.all()
    return render(request, 'discussion_forum/forum_home.html', {'topics': topics})

def topic_detail(request, topic_title):
    topic = get_object_or_404(Topic, title=topic_title)
    posts = topic.posts.all()
    return render(request, 'discussion_forum/topic_detail.html', {
        'topic': topic,
        'posts': posts,
    })

def forum_index(request):
    return render(request, 'discussion_forum/forum_index.html')
