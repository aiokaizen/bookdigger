from django.contrib import admin
from digger.models import Book, Author, Comment, Rating


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Rating)
