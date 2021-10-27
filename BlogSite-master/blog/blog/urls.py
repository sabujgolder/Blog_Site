
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Blog.urls')),
    path('user/',include('App_Login.urls')),
    # path('',views.home,name='home')
]
