from django.shortcuts import render
from posts.models import *
from posts.serializers import *
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from posts.permissions import IsOwnerOrReadOnly


# Create your views here.

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer): serializer.save(owner=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,) 

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class ProfilePost(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfilePosts
    name='profile-posts'


class PostComment(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class = PostComments
    name='posts-comments'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):

        return Response({
            'profiles': reverse(ProfileList.name,request=request),
            'posts': reverse(PostList.name,request=request),
            'comments' : reverse(CommentList.name,request=request),
            'profile-posts': reverse(ProfilePost.name,request=request),
            'posts-comments': reverse(PostComment.name,request=request),
            'users': reverse(UserList.name,request=request),


})