from .models import Blog_Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import Blog_PostSerializer


class Blog_PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog_Post.objects.all().order_by('-published_date')
    serializer_class = Blog_PostSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Blog_PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog_Post.objects.all()
    serializer_class = Blog_PostSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]


#Alternate views
"""
class Blog_PostViewSet(viewsets.ModelViewSet):
    queryset = Blog_Post.objects.all() 
    serializer_class = Blog_PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
"""

# Create your views here.
