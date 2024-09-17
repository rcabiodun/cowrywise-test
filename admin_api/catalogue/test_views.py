from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, User, BorrowedBook

class BookViewsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="Clean Code",
            author="Robert C. Martin",
            publisher="Prentice Hall",
            category="Technology",
            is_available=True
        )

    def test_add_book(self):
        response = self.client.post('/api/catalogue/add-book/', {
            'title': "New Book",
            'author': "New Author",
            'publisher': "New Publisher",
            'category': "Fiction",
            'is_available': True
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_remove_book(self):
        response = self.client.delete(f'/api/catalogue/remove-book/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_users(self):
        response = self.client.get('/api/catalogue/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_borrowed_books(self):
        response = self.client.get('/api/catalogue/borrowed-books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_unavailable_books(self):
        response = self.client.get('/api/catalogue/unavailable-books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
