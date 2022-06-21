from django.contrib import admin
from .models import Category, Book, Author,BorrowBook,User

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','image')



admin.site.register(Category)
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(BorrowBook)
admin.site.register(User)



