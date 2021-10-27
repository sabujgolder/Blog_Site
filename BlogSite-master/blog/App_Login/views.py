from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .forms import *

def register(request):
    form = SignUpForm()
    registered = False

    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form,'registered':registered}
    return render(request,'App_login/sign_up.html',context = dict)

def login_user(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                # return redirect('')
                return HttpResponseRedirect(reverse('blog:home'))
    return render(request,'App_login/login.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))

@login_required
def user(request):
    return HttpResponse("User")

@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    return render(request, 'App_Login/change_profile.html', context={'form':form})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'App_Login/pass_change.html', context={'form':form, 'changed':changed})
