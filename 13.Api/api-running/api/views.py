from django.shortcuts import render

from rest_framework import generics,permissions
from blog.models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly # new


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 

class BlogUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer       

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

