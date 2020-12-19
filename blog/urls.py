from django.urls import path
from blog.views import *
from django.conf.urls.static import static

urlpatterns = [
                  path('home/', home, name='home'),
                  path('categries/', show_all_categories, name='categories'),
                  path('posts/', ShowPosts.as_view(), name='posts'),
                  path('single_post/<slug:slug>', SinglePost.as_view(), name='post'),
                  path('cat_posts/<slug:slug>', CatPosts.as_view(), name='category')
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
