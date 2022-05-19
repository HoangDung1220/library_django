from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return render(request,'book_user/index.html')

def blog(request):
    return render(request,'book_user/blog.html')