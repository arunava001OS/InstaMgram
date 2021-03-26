from django.db import models

from accounts.models import Profile
from post.models import Post
# Create your models here.
class Follow(models.Model):
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    following = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='follower')
    date = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return "{} {} --> {} {} on {}".format(self.follower.firstname,self.follower.lastname,self.following.firstname,self.following.lastname,str(self.date))

class Like(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} --> {} {} on {}".format(self.author.firstname,self.author.lastname,self.post.author.firstname,self.post.author.lastname,str(self.post.date_created))

class Comment(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.CharField(max_length=100,default='')
