from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    queryset = Post.published.all()


class PostApiView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    queryset = Post.published.all()