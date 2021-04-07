from django.db import models

from accounts.models import Profile

# Create your models here.
class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-images/')
    caption = models.TextField(default="")
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.firstname +" "+ self.profile.middlename +" "+ self.profile.lastname + " - " + str(self.date)

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()