from celery import shared_task
import requests
from django.utils import timezone
from .models import Book

@shared_task
def sync_books_from_admin_api():
    print("running Task")
    # the host '172.27.0.1' is the gateway for the network the containers share
    admin_api_url = 'http://172.27.0.1:8000/api/catalogue/books/'
    try:
        response = requests.get(admin_api_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
        return

    books = response.json()
    for book_data in books:
        Book.objects.update_or_create(
            id=book_data['id'],
            defaults={
                'title': book_data['title'],
                'author': book_data['author'],
                'publisher': book_data['publisher'],
                'category': book_data['category'],
                'is_available': book_data['is_available'],
                'borrowed_until': book_data.get('borrowed_until', None),
            }
        )
