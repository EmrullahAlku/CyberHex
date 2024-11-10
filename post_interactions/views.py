from django.shortcuts import render, get_object_or_404
from .models import Comment
from discussion_forum.models import Post

def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_interactions/post_comments.html', {'post': post, 'comments': comments})

def interactions_index(request):
    return render(request, 'post_interactions/interactions_index.html')
