from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Comment

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
        

 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
 
class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['url','title','user', 'content']
 
class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
 
    class Meta:
        model = Comment
        fields = [ 'content', 'user']
        depth = 1