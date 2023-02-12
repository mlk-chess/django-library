from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Book, Borrow


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        book = Book(
            title=request.POST['title'],
            author=request.POST['author'],
            cover=request.FILES['cover'],
            publisher=request.POST['publisher'],
            collection=request.POST['collection'],
            genre=request.POST['genre']
        )
        book.save()
        return redirect('book_list')
    return render(request, 'book/book_form.html')


def book_update(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.cover = request.FILES['cover']
        book.publisher = request.POST['publisher']
        book.collection = request.POST['collection']
        book.genre = request.POST['genre']
        book.save()
        return redirect('book_list')
    return render(request, 'book/book_form.html', {'book': book})


def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('book_list')


def late_loans(request):
    late_books = Book.objects.filter(loan__returned_at__lt=timezone.now(), loan__returned=False)
    return render(request, 'library/late_loans.html', {'late_books': late_books})


def borrow_management(request):
    borrows = Borrow.objects.all()
    return render(request, 'library/borrow_management.html', {'borrows': borrows})