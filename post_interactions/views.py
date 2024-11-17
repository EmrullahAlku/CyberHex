from django.shortcuts import render, get_object_or_404
from .models import Comment
from discussion_forum.models import Post
from django.contrib.auth.decorators import login_required

def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_interactions/post_comments.html', {'post': post, 'comments': comments})

@login_required
def interactions_index(request):
    if not request.user.is_authenticated:
        return render(request, 'post_interactions/interactions_index.html', {'posts': []})
    
    user_posts = Post.objects.filter(author=request.user)  # author, Post modelinde kullanıcıyı refere etmelidir.
    return render(request, 'post_interactions/interactions_index.html', {'posts': user_posts})

