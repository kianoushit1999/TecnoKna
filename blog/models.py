from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), db_index=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("root_category"), related_name="category",
                               related_query_name="category")

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f"Your category title is {self.title} ."

