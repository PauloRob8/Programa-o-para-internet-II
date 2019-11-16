from rest_framework import serializers
from posts.models import *



class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url','pk','name','email','adress')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','title','body','url','userId')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url','pk','name','email','body','postId')





class Postinho(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url','title','body')

class ProfilePosts(serializers.HyperlinkedModelSerializer):
    posts = Postinho(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ('url','pk','name','posts')
    



