from django.rest_framework import serializers
from posts.models import *

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'updated', 'user', 'upvote_count')

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ('id', 'user', 'post')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'body', 'created')
