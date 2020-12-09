from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

# Register your models here.
class CategoryItemInline(admin.TabularInline):
    model = Category
    fields = ('title', 'slug', 'parent')
    extra = 1
    show_change_link = True

class PostItemInline(admin.TabularInline):
    model = Post
    fields = (('title', 'content'), ('author', 'draft'), 'published_at')
    extra = 1
    show_change_link = True

class SettingPostInline(admin.TabularInline):
    model = PostSetting
    fields = ('author', 'allow_discussion', 'post', 'comment')
    extra = 1
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    search_fields = ('title', 'slug')
    list_filter = ('parent',)
    list_display_links = ('parent',)

    inlines = [PostItemInline, CategoryItemInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('post_like', 'post_dislike')
    list_display = ('author', 'title', 'content', 'draft', 'published_at', 'category')
    search_fields = ('author', 'title', 'published_at', 'created_at')
    list_filter = ('category', 'author', 'draft')
    date_hierarchy = 'published_at'
    list_display_links = ('category', 'author', 'title')

    def be_draft(self, request, queryset):
        update = queryset.update(draft=True)
        self.message_user(request,
                          _('%d Your selected items become draft') % update)
    be_draft.short_description = "Active draft capability"

    def del_draft(self, request, queryset):
        update = queryset.update(draft=False)
        self.message_user(request,
                          _('%d Your selected items become draft') % update)
    del_draft.short_description = "removing draft capability"

    inlines = [SettingPostInline]
    actions = [be_draft, del_draft]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude = ('com_like', 'com_dislike')
    list_editable = ('situation',)
    list_display_links = ('author',)
    search_fields = ('author', 'situation')
    list_display = ('author', 'is_confirmed', 'situation', 'author', 'post', 'com_like', 'com_dislike')
    date_hierarchy = 'created_at'

admin.site.register(CommentLike)