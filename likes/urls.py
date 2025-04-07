from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, RatingViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'', LikeViewSet)
router.register(r'Rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>/', like_post),
]