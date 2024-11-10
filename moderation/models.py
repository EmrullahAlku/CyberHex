from django.db import models
from user_accounts.models import User
from discussion_forum.models import Post

class Report(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.reported_by.username} - {self.post.id}"
