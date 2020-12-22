from django import forms
from django.forms import TextInput, Textarea, CheckboxInput
from django.utils.translation import gettext_lazy as _
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'situation']
        widgets = {
            'content': Textarea(attrs={
                'placeholder': 'content of your comment',
                'style': 'resize:none;'
                         'width:available;'
                         'padding-top:50px',
                'class': 'py-2'
            }),
            'situation': CheckboxInput(attrs={})
        }