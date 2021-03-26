from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    #profile_picture = models.ImageField(upload_to='profile_pictures/')

    firstname = models.CharField(max_length=100,default='')
    middlename = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100,default = '')
    
    gender = models.CharField(max_length=1,choices = [('M','Male'),('F','Female'),('O','Others')],default='O')

    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def __str__(self) :
        if(self.middlename != ''):
            return "{} {} {}".format(self.firstname,self.middlename,self.lastname)
        else:
            return "{} {}".format(self.firstname,self.lastname)

@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user = instance)
        print("New Token Created !!!")
