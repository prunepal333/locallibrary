from django.db import models
import uuid #unique id generator
from django.urls import reverse
# Create your models here.

#Genre model
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the genre name: ")
    def __str__(self):
        return self.name

#Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Brief description of book:")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 character isbn code: ')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book: ')
    language = models.ManyToManyField('Language', help_text='Select a language for this book')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

#BookInstance model
class BookInstance(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    due_back = models.DateField(null=True, blank=True)
    BOOK_STATUS = (('m', 'Maintenance'),
                    ('o', 'On loan'),
                    ('a', 'Available'),
                    ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=BOOK_STATUS, blank=True, default='m', help_text='Book\'s availability')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    # imprint = models.CharField(max_length=200)
    # language = models.OneToOneField('Language', on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return f'{self.unique_id} ({self.book.title})'

#Author model
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="First Name")
    last_name = models.CharField(max_length=100, help_text="Last Name")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null = True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
#Language Model
class Language(models.Model):
    name = models.CharField(max_length=50, help_text='Language? (Eg: English, Hindi, Nepali, Bangla, Tamil, French)')
    def __str__(self):
        return self.name
