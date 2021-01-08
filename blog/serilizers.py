from rest_framework import serializers
from account.serilizers import UserSerilizers
from .models import *

class PostsSerilizers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    published_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.published_at = validated_data.get('published_at', instance.published_at)
        instance.save()
        return instance

class CommentSerilizers(serializers.ModelSerializer):
    authors_info = UserSerilizers(source='author', read_only=True)
    post_info = PostsSerilizers(source='post', read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"

# class CommentSerilizers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content = serializers.CharField()
#     author = UserSerilizers(read_only=True)
#     situation = serializers.BooleanField()
#     post = PostsSerilizers(read_only=True)
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.content = validated_data.get('content', instance.content)
#         instance.situation = validated_data.get('situation', instance.situation)
#         instance.save()
#         return instance