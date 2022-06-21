from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index,name="index" ),
    path('blog/',views.blog,name='blog'),
    path('books/search', views.BooksViewSearch.as_view(), name= 'search'),
    path('books/',views.BooksView.as_view(),name='books'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('authors/search', views.AuthorViewSearch.as_view(), name= 'searchAuthor'),
    path('books/detail/<int:BookId>',views.getBookBlogDetail,name='book-blog-detail'),
    path('blog-detail-home/<int:blogId>',views.getBlogDetailHome,name='blog-detail-home'),
    path('comment-home/',views.CommentHomeView.as_view(),name='comment-home'),
    path('information/',views.getInformation,name='information'),
    path('update-information/',views.UserView.as_view(),name='information-update'),





]
