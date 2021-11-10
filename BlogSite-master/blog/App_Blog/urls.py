
from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('createblog/',views.CreateBlog.as_view(),name='createblog'),
    path('bloglist/',views.BlogList.as_view(),name='bloglist'),
    path('blog_details/<str:pk>',views.blog_details,name='detail')
]
