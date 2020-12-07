from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), db_index=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name=_("root_category"), related_name="category",
                               related_query_name="category")

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f"Your category title is {self.title} ."


class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), db_index=True, unique=True)
    content = models.TextField(_('content'), blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('category'),
                                 related_name='posts',
                                 related_query_name='posts')
    draft = models.BooleanField(_('draft'), default=True, db_index=True)
    author = models.ForeignKey(User, verbose_name=_('author'), on_delete=models.CASCADE, related_query_name='posts',
                               related_name='posts')
    image = models.ImageField(_('image'), upload_to='images', blank=True, null=True)
    like = models.IntegerField(_('like'), default=True)
    created_at = models.DateTimeField(_('creation'), auto_now_add=True)
    updated_at = models.DateTimeField(_('update'), auto_now=True)
    published_at = models.DateTimeField(_('publish_time'), db_index=True)

    @property
    def add_like(self):
        self.like += 1
        self.save()

    @property
    def decrease_like(self):
        self.like -= 1
        self.save()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ["published_at", "created_at"]

    def __str__(self):
        return f"{self.title} and its category is {self.category}"

class Comment(models.Model):
    content = models.TextField(_('content'), default=True, null=True)
    is_confirmed = models.BooleanField(_('confirm'), default=True)
    like = models.IntegerField(_('like'), default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('author'), db_index=True)
    created_at = models.DateTimeField(_('creation'), auto_now_add=True)
    updated_at = models.DateTimeField(_('update'), auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'), related_name='comment', related_query_name='comment')

    @property
    def comment_like(self):
        self.like += 1
        self.save()

    @property
    def comment_dislike(self):
        self.like -= 1
        self.save()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        order_with_respect_to = ['created_at']

    def __str__(self):
        return f'comment: is written by {self.author}'

class PostSetting(models.Model):
    comment = models.OneToOneField(Comment, verbose_name=_("comment"), default=True, on_delete=models.CASCADE)
    author = models.BooleanField(_("author"), default=True)
    allow_discussion = models.BooleanField(_("allow_discuss"), default=True)
    post = models.OneToOneField(Post, verbose_name=_("post"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("setting")
        verbose_name_plural = _("settings")

    def __str__(self):
        return f'active to comment' if(self.allow_discussion) else f'inactive to commenting'