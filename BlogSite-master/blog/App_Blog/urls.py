
from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('createblog/',views.CreateBlog.as_view(),name='createblog'),
    path('bloglist/',views.BlogList.as_view(),name='bloglist'),
    path('blog_details/<str:pk>',views.blog_details,name='detail'),
    path('like/<str:pk>',views.likes,name='like'),
    path('unlike/<str:pk>',views.unlike,name='unlike'),
    path('update_blog/<str:pk>',views.update_blog,name='updateblog')
]
