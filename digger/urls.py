from django.urls import path

from digger.views import *

app_name = 'digger'

urlpatterns = [

    # Home
    path('', BookListView.as_view(), name="book_list"),
    path('books/', BookListView.as_view(), name="book_list"),
    path('books/<int:book_id>/', BookDetailsView.as_view(), name="book_details")
]
