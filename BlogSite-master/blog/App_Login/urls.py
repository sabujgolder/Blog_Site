from django.urls import path
from App_Login import views

app_name = "user"

urlpatterns = [
    path('',views.user,name='user'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('update_profile/',views.user_change,name='update_profile'),
    path('password/',views.pass_change,name='pass_change'),
    path('profile_pic/',views.profile_pic,name='profile_pic'),
    path('change_profile_pic/',views.change_pro_pic,name='change_pro_pic'),
]
