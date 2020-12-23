from django.shortcuts import render
from .models import Book, Author,BookInstance,Genre
# Create your views here.

#receive HttpRequest as parameter
def index(request):
    ''' View function for the home page of the site.'''
    #do some dancing
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres_science = Genre.objects.filter(name__icontains='science').count()
    num_books_data = Book.objects.filter(title__icontains='data').count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_data': num_books_data,
        'num_genres_science': num_genres_science,
    }
    #return HTML as response
    return render(request, 'index.html', context=context)