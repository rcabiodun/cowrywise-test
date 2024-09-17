from django.urls import path
from .views import AddBookView, RemoveBookView, ListUsersView, ListBorrowedBooksView, UnavailableBooksView,ListBooksView

urlpatterns = [
    path('add-book/', AddBookView.as_view(), name='add-book'),
    path('remove-book/<int:pk>/', RemoveBookView.as_view(), name='remove-book'),
    path('users/', ListUsersView.as_view(), name='list-users'),
    path('borrowed-books/', ListBorrowedBooksView.as_view(), name='list-borrowed-books'),
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('unavailable-books/', UnavailableBooksView.as_view(), name='unavailable-books'),
]
