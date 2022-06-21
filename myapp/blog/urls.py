from django.urls import path
from . import views

urlpatterns = [
    path('blog-book/<int:BookId>',views.getBookBlog,name='blog-book'),
    path('blog-personal/',views.BlogView.as_view(),name='blog-personal'),
    path('personal-home/',views.Personal.as_view(),name='personal_home'),
    path('blog-detail/<int:blogId>',views.getBlogDetail,name='blog-detail'),
    path('book-borrow/',views.BookBorrowView.as_view(),name='book-borrow'),
    path('comment/',views.CommentView.as_view(),name='comment'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('book-detail/',views.BookView.as_view(),name='book-detail'),
    path('blog-detail/',views.getBlogPersonal,name='blog-detail'),
    path('logout/',views.LogoutView.as_view(),name='log-out'),
    path('update-blog/',views.UpdateBlog.as_view(),name='update'),
    path('update-blog/<int:id_blog>',views.getUpdateBlog,name='update-blog'),
    path('blog-home/',views.getBlogHome,name='blog-home'),




]
