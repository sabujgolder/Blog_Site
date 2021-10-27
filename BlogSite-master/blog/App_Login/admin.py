from django.contrib import admin
from App_Blog.models import *
from App_Login.models import *

admin.site.register(UserProfile)
admin.site.register(blog)
admin.site.register(comment)
admin.site.register(like)
