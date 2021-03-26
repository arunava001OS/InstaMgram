from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer,ProfileSerializer

from accounts.models import Profile

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user = user)
            data['response'] = 'New User Successfully Created'
            data['email'] = user.email
            data['username'] = user.username
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_update_view(request):
    data = {}
    if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            profile,created = Profile.objects.get_or_create(user = request.user)
            profile.firstname = serializer.data['firstname']
            profile.middlename = serializer.data['middlename']
            profile.lastname = serializer.data['lastname']
            profile.gender = serializer.data['gender']
            profile.save()
        else:
            data = serializer.errors
    else:
        profile,created = Profile.objects.get_or_create(user = request.user)
    data['email'] = profile.user.email
    data['firstname'] = profile.firstname
    data['middlename'] = profile.middlename
    data['lastname'] = profile.lastname
    data['gender'] = profile.gender
    data['followers'] = profile.followers_count
    data['following'] = profile.following_count
    return Response(data)
        
