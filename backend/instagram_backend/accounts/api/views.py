from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.api.serializers import RegistrationSerializer

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user = user)
            data['response'] = 'New User Successfully Created'
            data['email'] = user.email
            data['username'] = user.username
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
def login_view(request):
    pass

@api_view(['GET','POST'])
def profile_update_view(request):
    pass