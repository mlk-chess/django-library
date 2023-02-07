from django.db import models


class Book(models.Model):

    class Meta:
        app_label = 'book'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/')
    publisher = models.CharField(max_length=200)
    collection = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

