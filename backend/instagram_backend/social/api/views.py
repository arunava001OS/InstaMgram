from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from accounts.models import Profile
from django.contrib.auth.models import User
from social.models import Followship
from accounts.api.serializers import ProfileSerializer

class FollowshipView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self,request):
        """get all the followers and following"""
        follow = Profile.objects.get(user = request.user)
        follower_list = Followship.objects.filter(follower = follow)
        following_list = Followship.objects.filter(following = follow)
        profile_follower_list = []
        profile_following_list = []
        for i in follower_list:
            profile_follower_list.append(i.following)
        for i in following_list:
            profile_following_list.append(i.following)
        result1 = ProfileSerializer(profile_following_list,many=True)
        result2 = ProfileSerializer(profile_follower_list,many=True)
        return Response({
            "follower":result1.data,
            "following":result2.data
        })


    def post(self,request):
        follower = Profile.objects.get(user = request.user)
        try:
            following = Profile.objects.get(user = User.objects.get(username =request.POST['username']))
            follow,created = Followship.objects.get_or_create(follower=follower,following = following)
            if(follower.user.username != following.user.username):
                if(created):
                    follow.save()
                    follower.following_count += 1
                    following.followers_count += 1
                    following.save()
                    follower.save()
                    return Response({'response':'Profile followed successfully'})
                else:
                    return Response({'response':'already followed that user'})
            else:
                return Response({'response':'action prohibited'})
        except:
            return Response({'response':'This service is unavailable right now.'})
    
    def delete(self,request):
        follower = Profile.objects.get(user = request.user)
        try:
            following = Profile.objects.get(user = User.objects.get(username =request.POST['username']))
            follow = Followship.objects.get(follower=follower,following = following)
            follower.following_count -= 1
            following.followers_count -= 1
            following.save()
            follower.save()
            follow.delete()
            return Response({'response':'Unfollowed successfully'})
        except:
            return Response({'response':'User not followed yet'})

