from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User
from django.core.exceptions import ValidationError
class SignUp(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailField,
            'password1': forms.PasswordInput,
            'password2': forms.PasswordInput
        }

        labels = {
            'user_name': _('User'),
            'first_name': _('First_name'),
            'last_name': _('Last_name'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm Password')
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This Username is too long."),
            }
        }

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            return ValidationError(_('Your inputed passwords is not compatible to each other'))
        return password1