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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.author.profile.comment_count += 1
        self.author.profile.update_level()

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.profile.like_count += 1
        self.user.profile.update_level() 
