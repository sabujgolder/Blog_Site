from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView,UpdateView,DetailView,TemplateView,CreateView,DeleteView,View
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .forms import *
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

    already_liked = like.objects.filter(author=request.user,blog=blog_name)
    blog_likes = like.objects.filter(blog=blog_name)
    total_likes =  blog_likes.count()

    if already_liked:
        like_signal = True

    else:
        like_signal = False

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog_name
            comment.save()
            return HttpResponseRedirect(reverse('blog:detail', kwargs={'pk':pk}))
    return render(request,'App_Blog/blog_details.html',{'blog':blog_name,'form':form,'likes':total_likes,'liked':like_signal})

def likes(request,pk):

    blog_name = blog.objects.get(id=pk)

    already_liked = like.objects.filter(blog=blog_name,author = request.user)

    if not already_liked:
        liked_post = like(author = request.user,blog=blog_name)
        liked_post.save()
    return HttpResponseRedirect(reverse('blog:detail', kwargs={'pk':pk}))


def unlike(request,pk):

    blog = blog.objects.get(id=pk)
    author = request.user
    already_liked = like.objects.filter(blog=blog,author = author)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog:detail', kwargs={'pk':pk}))
