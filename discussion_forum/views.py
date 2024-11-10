from django.shortcuts import render, get_object_or_404
from .models import Topic

def forum_home(request):
    topics = Topic.objects.all()
    return render(request, 'discussion_forum/forum_home.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'discussion_forum/topic_detail.html', {'topic': topic})

def index(request):
    return render(request, 'discussion_forum/index.html')
