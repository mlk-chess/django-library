from django.db import models
from book.models import Book;

app_label="library"

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
