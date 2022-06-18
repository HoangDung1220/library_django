from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index,name="index" ),
    path('blog/',views.blog,name='blog'),
    path('books/search', views.BooksViewSearch.as_view(), name= 'search'),
    path('books/',views.BooksView.as_view(),name='books'),
  

]
