from django.shortcuts import render,HttpResponseRedirect


def home(request):
    return render(request,'App_Blog/index.html')
