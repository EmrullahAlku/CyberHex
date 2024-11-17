from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    post_count = models.PositiveIntegerField(default=0)  
    like_count = models.PositiveIntegerField(default=0) 
    comment_count = models.PositiveIntegerField(default=0)  
    level = models.CharField(max_length=50, blank=True) 

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def update_level(self):
        total_interactions = self.post_count + self.like_count + self.comment_count
        if total_interactions < 50:
            self.level = 'Beginner'
        elif total_interactions < 100:
            self.level = 'Intermediate'
        else:
            self.level = 'Expert'
        self.save()
