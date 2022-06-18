from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Book


def index(request):
    return render(request,'book_user/index.html')

def blog(request):
    return render(request,'book_user/blog.html')

# def books(req):
#     books = Book.objects.all()
#     return render(req, 'book_user/books.html', {'books': books})

class BooksView(View):
    def get(seft, req):
        booklist = Book.objects.all()
        paginator = Paginator(booklist, 6)
        pageNumber = req.GET.get('page')
        try:
            book = paginator.page(pageNumber)
        except PageNotAnInteger:
            book = paginator.page(1)
        except EmptyPage:
            book = paginator.page(paginator.num_pages)
        
        return render(req, 'book_user/books.html', {'books': book})

class BooksViewSearch(View):
    def get(self, req):
        query = req.GET.get('s')
        if query != None:
            booklist = Book.objects.filter(name__icontains = query)
        else:
            booklist = Book.objects.all()
        paginator = Paginator(booklist, 6)
        pageNumber = req.GET.get('page')
        try:
            book = paginator.page(pageNumber)
        except PageNotAnInteger:
            book = paginator.page(1)
        except EmptyPage:
            book = paginator.page(paginator.num_pages)
        
        return render(req, 'book_user/books.html', {'books': book})


