from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_view(request):
    pass

@api_view(['POST'])
def login_view(request):
    pass

@api_view(['GET','POST'])
def profile_update_view(request):
    pass