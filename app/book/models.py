from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Book(models.Model):
    class Meta:
        app_label = 'book'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/')
    publisher = models.CharField(max_length=200)
    collection = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_back_at = models.DateTimeField()

    def __str__(self):
        return f"{self.borrower} borrowed {self.book} on {self.borrowed_at}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    loan_date = models.DateTimeField(default=timezone.now)
    returned_at = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.borrow.borrower} returned {self.borrow.book} on {self.returned_at}"
