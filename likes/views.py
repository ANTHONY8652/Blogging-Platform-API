from .serializers import LikeSerializer, RatingSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Like, Rating
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from blog_posts.models import Blog_Post

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_post(request, pk):
    post = get_object_or_404(Blog_Post, pk=pk)
    score = request.data.get('score')
    Rating.objects.update_or_create(user=request.user, post=post, defaults={'score': score})
    return Response({"message": "Rated"})