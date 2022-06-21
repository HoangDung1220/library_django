from django.contrib import admin
from tomlkit import date
from .models import Category, Book, Author, BorrowBook, User
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","description")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description", "year_pub", "price", "quantily", "author", "category","image")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description", "year_born")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "first_name","last_name","email","date_joined")

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ("book", "user","date_borrow", "status")
    
    def changelist_view(self, request, extra_context= None):
        
        chart_data = (
            BorrowBook.objects.annotate(date = TruncDay("date_borrow"))
            .values("date")
            .annotate(y = Count("id"))
            .order_by("-date")
        )
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        return super().changelist_view(request, extra_context = extra_context)

