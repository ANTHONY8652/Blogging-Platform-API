from django.db import models
from django.contrib.auth.models import User
from blog_posts.models import Blog_Post


class Comment(models.Model):
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, related_name='likes')
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
