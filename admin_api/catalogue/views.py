from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, User, BorrowedBook
from .serializers import BookSerializer, UserSerializer, BorrowedBookSerializer

# View to add a new book
class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# View to delete a book
class RemoveBookView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# View to list all users
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View to list users and their borrowed books
class ListBorrowedBooksView(APIView):
    def get(self, request):
        borrowed_books = BorrowedBook.objects.select_related('user', 'book')
        data = [
            {
                'user': f'{borrowed_book.user.first_name} {borrowed_book.user.last_name}',
                'email': borrowed_book.user.email,
                'book': borrowed_book.book.title,
                'borrow_date': borrowed_book.borrow_date,
                'return_date': borrowed_book.return_date
            }
            for borrowed_book in borrowed_books
        ]
        return Response(data)

# View to list unavailable books and their return dates
class UnavailableBooksView(APIView):
    def get(self, request):
        unavailable_books = Book.objects.filter(is_available=False)
        data = [
            {
                'title': book.title,
                'author': book.author,
                'borrowed_until': book.borrowed_until
            }
            for book in unavailable_books
        ]
        return Response(data)

class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer