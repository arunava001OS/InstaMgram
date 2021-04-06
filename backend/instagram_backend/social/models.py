from django.db import models
from accounts.models import Profile

# Create your models here.

class Followship(models.Model):
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.user.username + "---> " + self.following.user.username



