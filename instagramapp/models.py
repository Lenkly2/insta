from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to="media/",blank=True)
    theme = models.BooleanField(blank=True,default=0)

class Subscribers(models.Model):                                                                               
    following = models.ForeignKey(CustomUser,null=True,blank=True,related_name="folowingdb",on_delete=models.DO_NOTHING)
    follower = models.ForeignKey(CustomUser,null=True,blank=True,related_name="followerdb",on_delete=models.DO_NOTHING)
    
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    media = models.FileField(upload_to="media/")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser,related_name="likes_db")

    def total_likes(self):
        return self.likes.count()
    
class Coment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    media = models.FileField(upload_to="media/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser,related_name="likes_db2")
    
    def total_likes(self):
        return self.likes.count()

class Massage(models.Model):
    by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="by_people")
    to = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="to_people")
    massage = models.TextField()