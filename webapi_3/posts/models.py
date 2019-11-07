from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=275)
    userId = models.ForeignKey(Profile,related_name='profile',on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    body = models.CharField(max_length=275)
    postId = models.ForeignKey(Post,related_name='post',on_delete=models.CASCADE)