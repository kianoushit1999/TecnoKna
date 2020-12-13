from django.db import models
from django.utils.translation import ugettext_lazy as _
from TecnoKna import settings

#define User
User = settings.AUTH_USER_MODEL
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
        return f"category : {self.title} ."


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
    created_at = models.DateTimeField(_('creation'), auto_now_add=True)
    updated_at = models.DateTimeField(_('update'), auto_now=True)
    published_at = models.DateTimeField(_('publish_time'), db_index=True)

    @property
    def post_like(self):
        return Comment.objects.get(post=self, situation=True).count()

    @property
    def post_dislike(self):
        Comment.objects.get(post=self, situation=True).count()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ["published_at", "created_at"]

    def __str__(self):
        return f"Post : {self.title} and  {self.category}"

class Comment(models.Model):
    content = models.TextField(_('content'), default=True, null=True)
    is_confirmed = models.BooleanField(_('confirm'), default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('author'), db_index=True)
    situation = models.BooleanField(_('situation'), default=True)
    created_at = models.DateTimeField(_('creation'), auto_now_add=True)
    updated_at = models.DateTimeField(_('update'), auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'), related_name='comment',
                             related_query_name='comment')

    @property
    def com_like(self):
        return CommentLike.objects.get(comment=self, situation=True).count()

    @property
    def com_dislike(self):
        return CommentLike.objects.get(comment=self, situation=False).count()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['created_at']

    def __str__(self):
        return f'comment: is written by {self.author}'

class CommentLike(models.Model):
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='comment_like',
                               related_query_name='comment_like'
                               , on_delete=models.CASCADE)
    situation = models.BooleanField(_('situation'), default=True)
    comment = models.ForeignKey(Comment, verbose_name=_('comment'), on_delete=models.CASCADE, default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = 'comment_like'
        verbose_name_plural = 'comment_likes'
        unique_together = [['author', 'comment']]


class PostSetting(models.Model):
    comment = models.BooleanField(_("comment"), default=True)
    author = models.BooleanField(_("author"), default=True)
    allow_discussion = models.BooleanField(_("allow_discuss"), default=True)
    post = models.OneToOneField(Post, verbose_name=_("post"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("setting")
        verbose_name_plural = _("settings")

    def __str__(self):
        return 'active to commenting' if (self.allow_discussion) else 'inactive to commenting'