from rest_framework import serializers
from .models import Like, Rating
#from markdown import markdown


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'