from django.shortcuts import render
from posts.models import *
from posts.serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ProfilePosts(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePosts
    name='profile-posts'

class ProfilePostsDetail(generics.RetrieveUpdateDestroyAPIView):
    quersyset=Profile.objects.all()
    serializaer_class = ProfilePosts
    name='profile-posts-detail'

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):

        return Response({
            'profiles': reverse(ProfileList.name,
            request=request),
            'profile-posts': reverse(ProfilePosts.name,request=request),

})