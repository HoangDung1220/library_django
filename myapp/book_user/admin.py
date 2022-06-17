from re import A, U
from django.contrib import admin
from .models import Category, Book, Author, Role, BorrowBook, ReviewerBook, User

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","description")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description", "year_pub", "price", "quantily", "author", "category","image")
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description", "year_born")
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description")
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","name", "address","username","password","role")

@admin.register(BorrowBook)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ("book", "user","date_borrow", "status")
    
@admin.register(ReviewerBook)
class ReviewerBook(admin.ModelAdmin):
    list_display = ("book", "user", "title", "content")

