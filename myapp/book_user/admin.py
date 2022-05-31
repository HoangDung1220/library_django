from django.contrib import admin
from .models import Category, Book, Author

# class BookAdmin(admin.ModelAdmin):
#     list_display = ()


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
