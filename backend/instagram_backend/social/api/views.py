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
        follower = Profile.objects.get(user = request.user)
        following_list = Followship.objects.filter(follower = follower)
        profile_list = []
        for i in following_list:
            profile_list.append(i.following)
        result = ProfileSerializer(profile_list,many=True)
        return Response(result.data)


    def post(self,request):
        follower = Profile.objects.get(user = request.user)
        try:
            following = Profile.objects.get(user = User.objects.get(username =request.POST['username']))
            follow,created = Followship.objects.get_or_create(follower=follower,following = following)
            if(created):
                follow.save()
                return Response({'response':'Profile followed successfully'})
            else:
                return Response({'response':'already followed that user'})
        except:
            return Response({'response':'This service is unavailable right now.'})
    
    def delete(self,request):
        follower = Profile.objects.get(user = request.user)
        try:
            following = Profile.objects.get(user = User.objects.get(username =request.POST['username']))
            follow = Followship.objects.get(follower=follower,following = following)
            follow.delete()
            return Response({'response':'Unfollowed successfully'})
        except:
            return Response({'response':'User not followed yet'})

