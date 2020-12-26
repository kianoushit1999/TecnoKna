import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render
from django.urls import reverse
from .form import CommentForm
from .models import *
User = get_user_model()

# Create your views here.
def home(request):
    post_most_like_by_comment = Post.objects.filter(comment__situation__exact=True).order_by('comment__situation')
    print(post_most_like_by_comment)
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
        content = data.get('content', None)
        like = True if data.get('situation', None) == 'on' else False
        slug = self.kwargs.get('slug', None)
        author = self.request.user
        post = Post.objects.get(slug__exact=slug)
        Comment.objects.create(
            post=post,
            situation=like,
            author=author,
            content=content,
            is_confirmed=True
        )
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
@csrf_exempt
def comment_like(request):
    flag = True
    post_slug, pk, author = json.loads(request.body).split(',')
    post = Post.objects.get(slug=post_slug)
    comment = Comment.objects.get(Q(pk=int(pk)) & Q(post=post))
    user = User.objects.get(username=author)
    try:
        comment_like: CommentLike = CommentLike.objects.get(Q(author=user) & Q(comment__exact=comment))
        comment_like.delete()
        flag = False
    except Exception:
        CommentLike.objects.create(author=user, comment=comment)
    response = {
        "like": flag,
        "comment_id": comment.pk
    }
    return JsonResponse(response)