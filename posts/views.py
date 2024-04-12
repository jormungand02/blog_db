from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer, PostListSerializer

class PermissionMixin:
    def get_permission(self):
        if self.action in ('retrieve', 'list'):
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

class PostViewSet(PermissionMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class
    
    def get_serializer_context(self):
        return {'request':self.request}