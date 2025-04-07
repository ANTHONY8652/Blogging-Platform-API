from django.db import models
from django.contrib.auth.models import User

class Blog_Post(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Science', 'Science'),
        ('Gossip', 'Gossip'),
        ('Hot Goss', 'Hot Goss'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Kids', 'Kids'),
        ('Politics', 'Politics'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title + self.author

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

# Create your models here.
