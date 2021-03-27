from post.models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from accounts.models import Profile
from post.models import Post

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_post(request):
    profile = Profile.objects.get(user = request.user)
    post = Post.objects.create(profile = profile)
    post.image = request.data['image']
    post.caption = request.data['caption']
    post.save()
    data = {'response': "Post Created successfully !"}
    return Response(data)
