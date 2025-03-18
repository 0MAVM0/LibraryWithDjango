from django.shortcuts import render
from .models import Book

def home_page(request):
    books = Book.objects.all()
    context = { "books" : books }

    return render(request, "home.html", context)
