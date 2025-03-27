from .serializers import CommentSerializer
from .models import Comment
from rest_framework import viewsets

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Create your views here.
