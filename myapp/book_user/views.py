from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog,Comment

from .models import Book,Author,User

def index(request):
    booklist = Book.objects.all()[:3]
    authorlist = Author.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    return render(request,'book_user/index.html', {'booklist': booklist, 'author': authorlist,'blogs':blogs})

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

    
def getBookBlogDetail(request,BookId):
        b = Book.objects.filter(id=BookId)
        blogs = Blog.objects.filter(book_id=BookId)
        data = {
                'book':b[0],
                'blogs':blogs
                }
        return render(request,'book_user/book_detail_blog.html',data)

def getBlogDetailHome(request,blogId):
    blog = Blog.objects.get(pk=blogId)
    blogs = Blog.objects.filter(book_id = blog.book.id)[:5]
    comments = Comment.objects.filter(blog_id = blogId)
    data ={
        'blog':blog,
        'blogs':blogs,
        'comments':comments,
        'len':len(comments)
    }
   
    return render(request,'book_user/blog-details-home.html',data)


class CommentHomeView(View):
    def post(self,request):
        content = request.POST['content']
        comment_id = request.POST['id_comment']
        try:
            user_id = request.user.id
            user = User.objects.get(pk=user_id)
            blog_id = request.POST['id_blog']
            blog = Blog.objects.get(pk = blog_id)
            if (comment_id != ''):
                comment = Comment.objects.get(pk = int(comment_id))
                c = Comment(comment_branch=comment,content=content,user_send=user,blog=blog)
            else :
                c = Comment(content=content,user_send=user,blog=blog)

            c.save()
            print(content)
            return redirect('blog-detail-home',blogId = blog_id)
        except:
            return render(request,'book_user/login.html')

def getInformation(request):
    user = request.user
    data = {
        'user':user,

    }
    return render(request,'book_user/information.html',data)

class UserView(View):
    def post(self,request):
        user = request.user
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        user.username = username
        user.last_name = last_name
        user.first_name = first_name
        user.address = address
        user.email = email
        user.save()
        return redirect('information')
                                      
