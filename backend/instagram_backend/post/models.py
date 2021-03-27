from django.db import models

from accounts.models import Profile

# Create your models here.
class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-images/')
    caption = models.TextField(default="")
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

