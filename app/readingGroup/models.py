from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from book.models import Book;

class readingGroup(models.Model):
    class Meta:
        app_label = 'readingGroup'
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.name
