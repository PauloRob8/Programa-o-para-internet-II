from posts.serializers import *
import json

data = open('db.json','r')

json = json.load(data)

profiles = json['users']
posts = json['posts']
comments = json['comments']

def run():
    
    for i in profiles :
        profile_serializer = ProfileSerializer(data=i)
        if profile_serializer.is_valid():
            profile_serializer.save()

    for i in posts:
        post_serializer = PostSerializer(data=i)
        if post_serializer.is_valid():
            post_serializer.save()

    for i in comments:
        comment_serializer = CommentSerializer(data=i)
        if comment_serializer.is_valid():
             comment_serializer.save()

    print("\n Seu db.sqlite3 foi povoado com sucesso!")