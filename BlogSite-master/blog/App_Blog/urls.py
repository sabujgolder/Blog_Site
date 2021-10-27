
from django.urls import path
from App_Blog import views

app_name = "blog"

urlpatterns = [
    path('',views.home,name='home'),
]
