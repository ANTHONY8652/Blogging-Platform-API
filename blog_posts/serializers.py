from rest_framework import serializers
from .models import Blog_Post, Tag
from likes.models import Like, Rating
from markdown import markdown
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class Blog_PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    content_html = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    ratings_average = serializers.SerializerMethodField()

    class Meta:
        model = Blog_Post
        fields = '__all__'
        exclude = ['last_updated']

    def get_content_html(self, obj):
        return markdown(obj.content)
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_ratings_average(self, obj):
        return obj.ratings.aggregate(Rating.Avg('score'))['score__avg'] or 0

    def validate_date_time(self, value):
        from django.utils.timezone import now

        if value < now():
            raise serializers.ValidationError('Post date must be in the future it cannot be in the past')
        
        return value