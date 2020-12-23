from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    fieldsets = (
        ('Name', {
            'fields': ('first_name', 'last_name'),
        }),
        ('Date of Birth/Death', {
            'fields': ('date_of_birth', 'date_of_death'),
        })
    )

#If you don't use decorator as @admin.register(Author)
#Then, you should use admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.StackedInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','due_back','unique_id')
 