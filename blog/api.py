from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from blog.permissions import PostAccessPermission
from blog.serilizers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CategoriesViewSet(ModelViewSet):
    serializer_class = CategorySerilizers
    queryset = Category.objects.all()


class PostsViewSet(ModelViewSet):
    serializer_class = PostsSerilizers
    queryset = Post.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, PostAccessPermission]

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        post_comments = post.comment.all()
        serializer = CommentSerializers(post_comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.draft = False
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def post_setting(self, request, pk=None):
        post = self.get_object()
        setting = post.settings
        serializer = PostSettingSerializers(setting)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_published(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(draft=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    @action(detail=True, methods=['GET'])
    def comment_like(self, request, pk=None):
        comment = self.get_object()
        likes = comment.comments_like.all()
        serializer = CommentSerializers(likes, many=True)
        return Response(serializer.data)
