from django.urls import path
from rest_framework.routers import DefaultRouter
from TecnoKna.urls import router
from blog.api import *
from blog.views import *
from django.conf.urls.static import static

router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
                  path('home/', home, name='home'),
                  path('categries/', show_all_categories, name='categories'),
                  path('posts/', ShowPosts.as_view(), name='posts'),
                  path('single_post/<slug:slug>', SinglePost.as_view(), name='post'),
                  path('cat_posts/<slug:slug>', CatPosts.as_view(), name='category'),
                  path('comment_like/', comment_like, name='comment_like'),
                  path('comment/', comment, name='comment'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
