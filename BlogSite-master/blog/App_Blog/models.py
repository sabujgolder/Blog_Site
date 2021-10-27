from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title = models.CharField(max_length=264,null=True,blank=True,verbose_name='Put A Title')
    slug = models.CharField(max_length=264,unique=True,null=True,blank=True)
    blog_content = models.TextField(null=True,blank=True,verbose_name="what's on your mind")
    blog_image = models.ImageField(upload_to='profile_pics',verbose_name='Image',null=True,blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_author')
    blog = models.ForeignKey(blog,on_delete=models.CASCADE,related_name='user_comment')
    content = models.TextField(null=True,blank=True)

class like(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_blog')
    blog = models.ForeignKey(blog,on_delete=models.CASCADE,related_name='liked_user')
