from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render
from django.urls import reverse

from .form import CommentForm
from .models import *

# Create your views here.
def home(request):
    context = {}
    return render(request, 'blog/blog.html', context=context)

def show_all_categories(request):
    pass

@method_decorator(login_required, name='dispatch')
class ShowPosts(ListView):
    model = Post
    template_name = 'blog/posts.html'

@method_decorator(login_required, name='dispatch')
class SinglePost(DetailView, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context.get('post', None)
        context['comments'] = Comment.objects.filter(post=post)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        slug = self.kwargs.get('slug')
        return reverse('post', kwargs={'slug': slug})

    def form_valid(self, form):
        data = self.get_form_kwargs().get('data')
        print(data)
        print(self.kwargs)
        print(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class CatPosts(DetailView):
    model = Category
    template_name = 'blog/same_cat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context.get('category', None)
        context['posts'] = Post.objects.filter(category=category)
        return context