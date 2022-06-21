from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Book
from .models import Author


def index(request):
    booklist = Book.objects.all()[:3]
    authorlist = Author.objects.all()[:3]
    return render(request,'book_user/index.html', {'booklist': booklist, 'author': authorlist})

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

class AuthorView(View):
    def get(seft, req):
        authorlist = Author.objects.all()
        paginator = Paginator(authorlist, 6)
        pageNumber = req.GET.get('page')
        try:
            author = paginator.page(pageNumber)
        except PageNotAnInteger:
            author = paginator.page(1)
        except EmptyPage:
            author = paginator.page(paginator.num_pages)
        
        return render(req, 'book_user/author.html', {'authors': author})

class AuthorViewSearch(View):
    def get(self, req):
        query = req.GET.get('a')
        if query != None:
            authorlist = Author.objects.filter(name__icontains = query)
            # print(authorlist)
        else:
            authorlist = Author.objects.all()
        paginator = Paginator(authorlist, 6)
        pageNumber = req.GET.get('page')
        try:
            author = paginator.page(pageNumber)
        except PageNotAnInteger:
            author = paginator.page(1)
        except EmptyPage:
            author = paginator.page(paginator.num_pages)
        
        return render(req, 'book_user/author.html', {'authors': author})

    
