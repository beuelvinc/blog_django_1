from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-date"]
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True, related_name='comments')
    author=models.CharField(max_length=20,default="")
    text=models.TextField(default="")
    shared_comment=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-shared_comment"]
    def __str__(self):
        return self.author +" comment"