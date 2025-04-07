from .serializers import CommentSerializer
from .models import Comment
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from blog_posts.models import Blog_Post
from likes.models import Like


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Blog_Post, pk=pk)
    Like.objects.get_or_create(user=request.user, post=post)
    return Response({"message": "Liked"})

# Create your views here.
