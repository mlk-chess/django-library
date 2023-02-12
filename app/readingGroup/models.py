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
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None, null=True, blank=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name
