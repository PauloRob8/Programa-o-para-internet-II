from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','pk','username')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('street','suite','city','zipcode')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Profile
        fields = ('url','pk','owner','name','email','address')
    
    def create(self,validated_data):
        request_address = validated_data.pop('address')
        address = Address.objects.create(**request_address)
        return Profile.objects.create(address=address, **validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.address.street = validated_data.get('street',instance.address.street)
        instance.address.suite = validated_data.get('suite',instance.address.suite)
        instance.address.city = validated_data.get('city',instance.address.city)
        instance.address.zipcode = validated_data.get('zipcode',instance.address.zipcode)
        instance.save()
        return instance

class PostSerializer(serializers.HyperlinkedModelSerializer):
    userId = serializers.SlugRelatedField(queryset=Profile.objects.all(),slug_field='name')
    class Meta:
        model = Post
        fields = ('pk','title','body','url','userId')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.SlugRelatedField(queryset=Profile.objects.all(),slug_field='email')
    class Meta:
        model = Comment
        fields = ('url','pk','email','postId','name','body')


class CommentForPost(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url','name','body')

class PostComments(serializers.HyperlinkedModelSerializer):
    comments = CommentForPost(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ('url','title','body','comments')


class Postinho(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url','title','body')

class ProfilePosts(serializers.HyperlinkedModelSerializer):
    posts = Postinho(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ('url','pk','name','posts')

    



