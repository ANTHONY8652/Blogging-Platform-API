from .models import Blog_Post
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import Blog_PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BlogPostFilter


class Blog_PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog_Post.objects.all().order_by('-published_date')
    serializer_class = Blog_PostSerializer
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'content','published_date', 'author__username', 'tags__name']

    filterset_fields = ['published_date', 'category']

    ordering_fields = ['published_date', 'category']

    filterset_class = BlogPostFilter

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
