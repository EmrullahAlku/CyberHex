from django.shortcuts import render, get_object_or_404
from .models import Topic
from .models import Category, Post

def topic_detail(request, topic_title):
    topic = get_object_or_404(Topic, title=topic_title)
    posts = topic.posts.all()
    return render(request, 'discussion_forum/topic_detail.html', {
        'topic': topic,
        'posts': posts,
    })

def forum_index(request):
    categories = Category.objects.prefetch_related('topics').all()
    latest_posts = Post.objects.select_related('author', 'topic').order_by('-created_at')[:5]
    return render(request, 'discussion_forum/forum_index.html', {
        'categories': categories,
        'latest_posts': latest_posts,
    })

def category_topics(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topics.all()
    return render(request, 'discussion_forum/category_topics.html', {
        'category': category,
        'topics': topics,
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    return render(request, 'post_detail.html', {'post': post})
