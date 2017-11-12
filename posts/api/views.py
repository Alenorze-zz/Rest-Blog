from rest_framework.generics import (
    ListAPIView,
    RetriveAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostDetailAPIView(RetriveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


