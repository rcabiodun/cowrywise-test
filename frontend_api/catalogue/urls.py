from django.urls import path
from .views import EnrollUserView, ListAvailableBooksView, GetBookByIdView, FilterBooksView, BorrowBookView

urlpatterns = [
    path('enroll/', EnrollUserView.as_view(), name='enroll-user'),
    path('books/available/', ListAvailableBooksView.as_view(), name='list-available-books'),
    path('books/<int:pk>/', GetBookByIdView.as_view(), name='get-book-by-id'),
    path('books/', FilterBooksView.as_view(), name='filter-books'),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
]
