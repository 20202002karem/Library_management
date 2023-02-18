from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    books = Book.objects.all()
    catgory = Catgory.objects.all()
    return render(request, 'pages/index.html', {
        'books': books,
        'catogry': catgory,
        })

def books(request):
    catgory = Catgory.objects.all()
    books = Book.objects.all()
    for i in books:
        print(i.photo_book,"---------------------------------------")
    return render(request, 'pages/books.html', {
        'catgory' : catgory,
        'books' : books,
    })

def delete(request):
    return render(request, 'pages/deletes.html', {})

def update(request):
    return render(request, 'pages/update.html', {})