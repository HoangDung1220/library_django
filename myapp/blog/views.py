from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.pyplot import title
from matplotlib.style import use
from .forms import BlogForm
from django.views import View
from book_user.models import Book,BorrowBook
from blog.models import Blog,Comment
from book_user.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookBorrowView(View):
    def get(self,request):
        id = request.user.id
        list = BorrowBook.objects.filter(user_id=id)
        data ={
            'list':list
        }
        return render(request,'book_user/book_borrow.html',data)

def getBookBlog(request,BookId):
        f = BlogForm()
        b = Book.objects.filter(id=BookId)
        blogs = Blog.objects.filter(book_id=BookId)
        data = {
                'f':f,
                'book':b[0],
                'blogs':blogs
                }
        return render(request,'book_user/create_blog.html',data)

def getBlogDetail(request,blogId):
    blog = Blog.objects.get(pk=blogId)
    blogs = Blog.objects.filter(book_id = blog.book.id)[:5]
    comments = Comment.objects.filter(blog_id = blogId)
    data ={
        'blog':blog,
        'blogs':blogs,
        'comments':comments,
        'len':len(comments)
    }
   
    return render(request,'book_user/blog-details.html',data)

class CommentView(View):
    def post(self,request):
        content = request.POST['content']
        comment_id = request.POST['id_comment']
       
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
        return redirect('blog-detail',blogId = blog_id)

class BlogView(View):
    def post(self,request):
        f = BlogForm(request.POST, request.FILES)
        BookId = request.POST['id_book']
        book = Book.objects.get(pk=BookId)
        user = request.user
        if f.is_valid():
            title = f.cleaned_data['title']
            image = f.cleaned_data['image']
            content = f.cleaned_data['content']
            blog = Blog(title=title,book=book,user=user,content=content,image=image)
            blog.save()
        return redirect('blog-book', BookId=BookId)

    def get(self,request):
        id = request.user.id
        list = Blog.objects.filter(user_id=id)
        data = {
            'list':list
        }
        return render(request,'book_user/blog.html',data)
    
class Personal(LoginRequiredMixin,View):    
    login_url = '/login'
    def get(self,request):
        booklist = Book.objects.all()
        return render(request,'book_user/personal_home.html',{'list':booklist})

class LoginView(View):
    def get(self,request):
        return render(request,'book_user/login.html')
    
    def post(self,request):
        username = request.POST.get('userName')
        password = request.POST.get('password')
         
        user_auth = authenticate(request,username= username,password=password)
        if user_auth !=None:
            login(request,user_auth)
            booklist = Book.objects.all()
            return render(request,'book_user/personal_home.html',{'list':booklist})
        else:
            return render(request,'book_user/login.html')
    



            

