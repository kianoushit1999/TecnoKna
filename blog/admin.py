from django.contrib import admin
from .models import *

# Register your models here.
class CategoryItemInline(admin.TabularInline):
    model = Category
    fields = ('title', 'slug', 'parent')
    extra = 1
    show_change_link = True

class postItemInline(admin.TabularInline):
    model = Post
    fields = (('title', 'content'), ('author', 'draft'), 'published_at')
    extra = 1
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    search_fields = ('title', 'slug')
    list_filter = ('parent',)
    list_display_links = ('parent',)

    inlines = [postItemInline, CategoryItemInline]
