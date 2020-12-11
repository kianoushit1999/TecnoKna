from django.urls import path
from blog.views import *

urlpatterns = [
    path('home/', home),
    path('categries/', show_all_categories),
    path('posts/', show_posts),
    path('signin/', sign_in),
    path('sign_up/', sign_up),
    path('single_post/<slug:pk>', single_post),
    path('cat_posts/<str:category>', cat_posts)
]
