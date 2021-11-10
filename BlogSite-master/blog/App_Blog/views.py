from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView,UpdateView,DetailView,TemplateView,CreateView,DeleteView,View
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
def home(request):
    return render(request,'App_Blog/index.html')

class CreateBlog(LoginRequiredMixin,CreateView):
    model = blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = blog
    template_name = 'App_Blog/blog_list.html'

def blog_details(request,pk):

    blog_name = blog.objects.get(id=pk)

    return render(request,'App_Blog/blog_details.html',{'blog':blog_name})
