from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import PostSerializer
from post.models import Post
from accounts.models import Profile

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        profile = Profile.objects.get(user = request.user)
        post = Post.objects.create(author = profile)
        post.image = serializer.data['image']
        post.caption = serializer.data['caption']
        post.save()
        data['author'] = post.author.user.username
        data['image'] = post.image
        data['caption'] = post.caption
        data['date'] = post.date_created
    else:
        data = serializer.errors
    return Response(data)
def delete_post(request):
    pass