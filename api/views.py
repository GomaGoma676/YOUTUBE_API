from rest_framework import viewsets
from rest_framework import generics
from .serializers import VideoSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .models import Video

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer