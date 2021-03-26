from django.db.models import fields
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    image = serializers.ImageField()
    caption = serializers.CharField(required=False, allow_blank=True,default = '', max_length=700) 
