from ctypes import addressof
from pyexpat import model
import black
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    year_born = models.IntegerField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(max_length= 10000, default='')

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(max_length=10000, default='')
    year_pub = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    quantily = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class BorrowBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrow = models.DateField()
    status = models.BooleanField()
    
    def __str__(self):
        return self.user.name
class ReviewerBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    def __str__(self):
        return self.book.name
    
    