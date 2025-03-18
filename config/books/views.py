from django.shortcuts import render
from .models import Book

def home_page(request):
    books = Book.objects.all()
    context = { "books" : books }

    return render(request, "home.html", context)

def detail_page(request, id):
    book = Book.objects.filter(id=id).first()
    context = { "book" : book }

    return render(request, "detail.html", context)