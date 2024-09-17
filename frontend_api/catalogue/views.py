from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, User, BorrowedBook
from .serializers import BookSerializer, UserSerializer

class EnrollUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListAvailableBooksView(generics.ListAPIView):
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer

class GetBookByIdView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FilterBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        publisher = self.request.query_params.get('publisher')
        category = self.request.query_params.get('category')
        queryset = Book.objects.all()

        if publisher:
            queryset = queryset.filter(publisher=publisher)
        if category:
            queryset = queryset.filter(category=category)

        return queryset

class BorrowBookView(APIView):
    def post(self, request):
        book_id = request.data.get('book_id')
        duration_days = int(request.data.get('duration_days'))
        try:
            book = Book.objects.get(pk=book_id)
            if not book.is_available:
                return Response({'error': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)

            user, created = User.objects.get_or_create(
                email=request.data.get('email'),
                defaults={
                    'first_name': request.data.get('first_name'),
                    'last_name': request.data.get('last_name')
                }
            )

            borrow_date = timezone.now().date()
            return_date = borrow_date + timezone.timedelta(days=duration_days)
            BorrowedBook.objects.create(
                user=user,
                book=book,
                borrow_date=borrow_date,
                return_date=return_date
            )

            book.is_available = False
            book.borrowed_until = return_date
            book.save()

            return Response({'message': 'Book borrowed successfully'})
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
