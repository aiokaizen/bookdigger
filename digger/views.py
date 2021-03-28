from django.views import View
from django.shortcuts import render

from digger.models import Book


class SignInView(View):

    def get(self, request):
        context = {

        }
        return render(request, 'digger/sign_in.html', context)


class SignOutView(View):

    def get(self, request):
        context = {

        }
        return render(request, 'digger/sign_out.html', context)


class SignUpView(View):

    def get(self, request):
        context = {

        }
        return render(request, 'digger/sign_up.html', context)


class BookListView(View):

    def get(self, request):

        books = Book.objects.all()

        context = {
            'queryset': books,
        }
        return render(request, 'digger/book_list.html', context)


class BookDetailsView(View):
    
    def get(self, request, book_id):
        
        book = Book.objects.get(pk=book_id)

        context = {
            'instance': book,
        }

        return render(request, 'digger/book_details.html', context)
