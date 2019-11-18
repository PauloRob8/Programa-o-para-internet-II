from django.shortcuts import render
from posts.models import *
from posts.serializers import *
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from posts.permissions import *
from rest_framework.authtoken.views import obtain_auth_token


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
    #def perform_create(self,serializer): serializer.save(userId=)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyPost )

class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyComment)


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (permissions.IsAdminUser,)


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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
        'token': token.key,
        'user_id': user.pk,
        'name': user.username
})