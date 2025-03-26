from django.urls import path, include
from .views import Blog_PostListCreateAPIView, Blog_PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list/', Blog_PostListCreateAPIView.as_view(), name='blog-post-list-create'),
    path('retrieve/', Blog_PostRetrieveUpdateDestroyAPIView.as_view(), name='blog-post-retrieve-update-destroy'),
]