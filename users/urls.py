from django.urls import path
from .views import UserDetailView, UserListCreateView, UserLoginView, UserLogoutView, ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile/', ProfileViewSet)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-register'),
    path('<int:pk>/', UserDetailView.as_view(), name='User-detail'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]