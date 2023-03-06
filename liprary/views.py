from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import BookForm
from .forms import BookForm, CatgoryForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        
        add_catgory = CatgoryForm(request.POST)
        if add_catgory.is_valid():
            add_catgory.save()
    books = Book.objects.all()
    catgory = Catgory.objects.all()
    
    return render(request, 'pages/index.html', {
        'books': books,
        'catgory': catgory,
        'form': BookForm(),
        'formcat': CatgoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailble': Book.objects.filter(status='avilble').count(),
        })

def books(request):
    catgory = Catgory.objects.all()
    search = Book.objects.all()
    title =None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    return render(request, 'pages/books.html', {
        'catgory' : catgory,
        'books' : search,
        'formcat': CatgoryForm(),
        'form': BookForm(),
    })

def delete(request, id):
    book_delete = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/deletes.html', {})

def update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES, instance=book )
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm( instance=book)
    return render(request, 'pages/update.html', {'form':form})