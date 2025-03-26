from rest_framework import serializers
from .models import Blog_Post, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class Blog_PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Blog_Post
        fields = '__all__'
        exclude = ['last_updated']

    def validate_date_time(self, value):
        from django.utils.timezone import now

        if value < now():
            raise serializers.ValidationError('Post date must be in the future it cannot be in the past')
        
        return value