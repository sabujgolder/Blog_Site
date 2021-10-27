from django.contrib import admin
from App_Blog.models import *
# Register your models here.

admin.site.register(blog)
admin.site.register(comment)
admin.site.register(like)
