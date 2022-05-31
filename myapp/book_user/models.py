import black
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    year_born = models.DateTimeField()
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
    year_pub = models.DateTimeField()
    price = models.FloatField(default=0)
    quantily = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=10000, default='')
    def __str__(self):
        return self.name
