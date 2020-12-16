from django.urls import path
from blog.views import *
from django.conf.urls.static import static

urlpatterns = [
                  path('home/', home, 'home'),
                  path('categries/', show_all_categories, 'categories'),
                  path('posts/', show_posts, 'posts'),
                  path('signin/', sign_in, 'signin'),
                  path('sign_up/', sign_up, 'signup'),
                  path('single_post/<slug:pk>', single_post, 'post'),
                  path('cat_posts/<str:category>', cat_posts, 'category')
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
