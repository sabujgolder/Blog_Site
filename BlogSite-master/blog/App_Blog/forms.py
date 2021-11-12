from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('content',)
