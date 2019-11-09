from rest_framework import serializers
from posts.models import *


class PostSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(),slug_field='name')
    class Meta:
        model = Post
        fields = ('title','body','userId')


class ProfilePosts(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ('url','pk','name','posts')
    

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url','pk','name','email','adress')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')
    class Meta:
        model = Comment
        fields = ('url','pk','post','body')

