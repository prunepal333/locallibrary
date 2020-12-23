from django.shortcuts import render
from .models import Book, Author,BookInstance, Genre
from django.views import generic
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
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='data')[:5]
    template_name = 'books/book_list.html'
    paginate_by = 2
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors/author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
