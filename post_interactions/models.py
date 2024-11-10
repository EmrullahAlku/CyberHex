from django.db import models
from user_accounts.models import User
from discussion_forum.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.post.topic.title}"

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
