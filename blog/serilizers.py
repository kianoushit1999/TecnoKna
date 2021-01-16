from rest_framework import serializers
from account.serilizers import UserSerilizers
from .models import *

class CategorySerilizers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class PostsSerilizers(serializers.ModelSerializer):
    author_info = UserSerilizers(source='author', read_only=True)
    category_info = CategorySerilizers(source='category', read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'draft',
            'category_info',
            'author_info'
        ]

class CommentSerilizers(serializers.ModelSerializer):
    authors_info = UserSerilizers(source='author', read_only=True)
    post_info = PostsSerilizers(source='post', read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"


class PostSettingSerializers(serializers.ModelSerializer):

    class Meta:
        model = PostSetting
        fields = "__all__"
