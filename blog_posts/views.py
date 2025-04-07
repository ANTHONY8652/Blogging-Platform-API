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

    def get_queryset(self):
        queryset = Blog_Post()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_draft=False)
        search = self.request.query_params.get('search')
        category = self.request.query_params.get('category')
        if search:
            queryset = queryset.filter(Blog_Post.Q(title__icontains=search) | Blog_Post.Q(content__icontains=search))
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        return queryset

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
