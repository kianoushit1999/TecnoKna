from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import phone_validator, pass_validator


class SignUpForm(forms.Form):
    user_name = forms.CharField(
        label=_('UserName'),
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={'style': 'width:40%;'
                            'border:2px solid rgb(75,203,240);'
                            'outline:none;'
                            'border-radius:7px;'
                            'padding:5px'
                   })
    )

    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={'style': 'width:40%;'
                            'border:2px solid rgb(75,203,240);'
                            'outline:none;'
                            'border-radius:7px;'
                            'padding:5px'
                   })
    )
    phone = forms.CharField(
        validators=[phone_validator()],
        label=_('Phone'),
        required=True,
        widget=forms.TextInput(attrs={'style': 'width:40%;'
                                               'border:2px solid rgb(75,203,240);'
                                               'outline:none;'
                                               'border-radius:7px;'
                                               'padding:5px'
                                      })
    )
    password = forms.CharField(
        label=_('password'),
        required=True,
        widget=forms.PasswordInput(attrs={'style': 'width:40%;'
                                                   'border:2px solid rgb(75,203,240);'
                                                   'outline:none;'
                                                   'border-radius:7px;'
                                                   'padding:5px'
                                          })
    )
    password2 = forms.CharField(
        label=_('confirm password'),
        required=True,
        widget=forms.PasswordInput(attrs={'style': 'width:40%;'
                                                   'border:2px solid rgb(75,203,240);'
                                                   'outline:none;'
                                                   'border-radius:7px;'
                                                   'padding:5px'
                                          })
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
