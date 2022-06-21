from django.db import models
from django.contrib.auth.models import User,AbstractUser

class User(AbstractUser):
    address = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    year_born = models.IntegerField()
    image = models.ImageField(upload_to = 'book_user/img/authors', default='')
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
    year_pub = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    quantily = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'book_user/img/books')
    def __str__(self):
        return self.name

class BorrowBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_borrow = models.DateField()
    date_pay = models.DateField()
    status = models.BooleanField(default=True)
    money = models.FloatField(default=0)
    def __str__(self):
        return self.user.username
   