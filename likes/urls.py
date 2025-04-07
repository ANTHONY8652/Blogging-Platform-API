from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register(r'', LikeViewSet)
router.register(r'Rating', RatingViewSet)