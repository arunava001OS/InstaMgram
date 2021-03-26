from django.db import models

from accounts.models import Profile

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post_images/')
    caption = models.CharField(max_length=700,default='')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.author.firstname,self.author.lastname,str(self.date_created))
    """
    def get_likes_count(self):
        return Like.objects.filter(post = self).count() 
    def get_comments_count(self):
        return Comment.objects.filter(post = self).count()
    def get_likes(self):
        likes_queryset = Like.objects.filter(post = self)
        likes_array = [i for i in likes_queryset]
        return likes_array
    def get_comments(self):
        comments_queryset = Comment.objects.filter(post = self)
        comments_array = [i for i in comments_queryset]
        return comments_array
    """