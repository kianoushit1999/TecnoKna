from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import phone_validator, pass_validator

class SignUpForm(forms.Form):

    user_name = forms.CharField(
        label=_('UserName'),
        max_length=120,
        required=True,
        widget=forms.TextInput()
    )

    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        validators=[phone_validator()],
        label=_('Phone'),
        required=True,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label=_('password'),
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_('confirm password'),
        required=True,
        widget=forms.PasswordInput()
    )

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password2', None)
        print(password, password2)
        if password != password2:
            raise ValidationError(_('Your inputed passwords is not compatible to each other'))

    def clean_password(self):
        password = self.cleaned_data.get('password', None)
        if not pass_validator(password):
            raise ValidationError(_('Your password must be contained alphanumeric and digit'))
        return password