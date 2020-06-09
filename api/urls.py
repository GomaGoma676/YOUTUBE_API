from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import VideoViewSet, CreateUserView

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('',include(router.urls)),
]