from django.db import models
from user_accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name="topics", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.topic.title}"
