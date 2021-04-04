from rest_framework import serializers

from post.models import Post
from accounts.models import Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','image','caption','likes','date']

    def create(self,validated_data):
        user =  self.context['request'].user
        profile = Profile.objects.get(user = user)
        post = Post.objects.create(profile = profile)
        post.image = validated_data.get('image')
        post.content = validated_data.get('caption')
        post.save()
        return post