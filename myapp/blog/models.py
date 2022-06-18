from turtle import update
from django.db import models
from matplotlib import widgets
from book_user.models import User

from book_user.models import Book

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    #create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/img')

class Comment(models.Model):
    
    create_date = models.DateTimeField(auto_now_add=True)
    user_send = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    comment_branch = models.ForeignKey('Comment',on_delete=models.CASCADE,blank=True,null=True,related_name="comment_items")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self) :
        return self.content

