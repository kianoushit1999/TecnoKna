from django.urls import path

from blog.api import *
from blog.views import *
from django.conf.urls.static import static

post_list = PostsInfo.as_view({
    'get': 'list',
    'post': 'create'
})

post_details = PostsInfo.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentInfo.as_view({
    'get': 'list',
    'post': 'create'
})

comment_details = CommentInfo.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
                  path('home/', home, name='home'),
                  path('categries/', show_all_categories, name='categories'),
                  path('posts/', ShowPosts.as_view(), name='posts'),
                  path('single_post/<slug:slug>', SinglePost.as_view(), name='post'),
                  path('cat_posts/<slug:slug>', CatPosts.as_view(), name='category'),
                  path('comment_like/', comment_like, name='comment_like'),
                  path('comment/', comment, name='comment'),
                  path('api/posts/', post_list, name="api_posts_list"),
                  path('api/posts/<int:pk>', post_details, name="api_post_details"),
                  path('api/comments/', comment_list, name="api_comments_list"),
                  path('api/comments/<int:pk>', comment_details, name="api_comments_details")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
