from django.urls import path

from digger.views import sign_in, sign_up, sign_out, books, book_details

app_name = 'digger'

urlpatterns = [

    # Home
    path('', books, name="books"),
    path('books/', books, name="books"),
    path('books/<int:book_id>/', book_details, name="book_details")
]
