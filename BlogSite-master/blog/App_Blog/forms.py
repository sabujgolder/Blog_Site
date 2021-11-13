from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('content',)

class BlogUpdate(forms.ModelForm):

    class Meta:
        model = blog
        fields = ('blog_title','blog_content','blog_image')
