from posts.serializers import *
import json

data = open('db.json','r')

json = json.load(data)

profiles = json['users']


def run():
    
    print(profiles)