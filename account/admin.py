from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AdminPasswordChangeForm

# Register your models here.
class phoneInlineForm(admin.TabularInline):
    model = User
    fields = ['phone', 'owner']
    extra = 1
    show_change_link = True

@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = ['email', 'is_staff', 'country']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email', 'country')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    inlines = [phoneInlineForm]