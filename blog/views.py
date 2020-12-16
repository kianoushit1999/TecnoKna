from django.shortcuts import render
from  .models import *

# Create your views here.
def home(request):
    context = {}
    return render(request, 'blog/blog.html', context=context)
def show_all_categories(request):
    pass

def show_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context=context)

def sign_in(request):
    pass

def sign_up(request):
    pass

def single_post(request, pk):
    pass

def cat_posts(request, category):
    pass
