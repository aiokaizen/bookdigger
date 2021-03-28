from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    title = models.CharField(verbose_name="Title", max_length=255)
    isbn = models.CharField(
        verbose_name="ISBN", max_length=13, default='', blank=True, 
        help_text="10 or 13 characters based code."
    )
    description = models.TextField()
    publication_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=57, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(verbose_name="First name", max_length=57)
    last_name = models.CharField(verbose_name="Last name", max_length=57)
    bio = models.TextField(null=True, blank=True)
    nationality = models.CharField(verbose_name="Nationality", max_length=57, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Rating(models.Model):
    
    value = models.PositiveSmallIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.book + ' ' + self.value


class Comment(models.Model):

    comment = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment if len(self.comment) < 150 else self.comment[:150] + '...'
