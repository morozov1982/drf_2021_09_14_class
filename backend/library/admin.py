from django.contrib import admin

from library.models import Author, Biography, Book

admin.site.register(Author)
admin.site.register(Biography)
admin.site.register(Book)