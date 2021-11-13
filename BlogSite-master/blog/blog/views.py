from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponseRedirect(reverse('blog:bloglist'))
