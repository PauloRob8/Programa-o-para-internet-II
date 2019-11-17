from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)


class Profile(models.Model):
    owner = models.ForeignKey('auth.User',related_name='posts',on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.OneToOneField(Address, models.CASCADE, related_name='address')

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=275)
    userId = models.ForeignKey(Profile,related_name='posts',on_delete=models.CASCADE)



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.ForeignKey(Profile,related_name='comment',on_delete=models.CASCADE)
    body = models.CharField(max_length=75)
    postId = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)