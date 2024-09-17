# Library Management System APIs

This project consists of two separate APIs designed to manage a library system: an **Admin API** for administrative tasks and a **Frontend API** for user interactions. Both APIs are built using Django and are deployed using Docker containers locally for development and testing purposes.

## Features

### Admin API

- **Add Books:** Admins can add new books to the library's catalog.
- **Remove Books:** Admins can remove books from the catalog.
- **List Users:** Fetch a list of users enrolled in the library.
- **List Borrowed Books:** Fetch a list of users along with the books they have borrowed.
- **Check Availability:** List books that are not currently available for borrowing, along with their next available dates.

### Frontend API

- **User Enrollment:** Users can enroll into the library using their email, firstname, and lastname.
- **Browse Books:** Users can list all available books in the catalog.
- **Book Details:** Users can retrieve details of a single book by its ID.
- **Filter Books:** Users can filter books by publishers (e.g., Wiley, Apress, Manning) or by category (e.g., fiction, technology, science).
- **Borrow Books:** Users can borrow books by specifying the book ID and the duration in days.

## Architecture

- **Two Separate Services:** Each API is designed as a separate service with its own database to ensure modularity and scalability.
- **Communication:** Changes in the Admin API (like adding a new book) trigger updates in the Frontend API via polling, implemented using Celery tasks.

## Technologies Used

- **Django:** Primary framework for both APIs.
- **SQLite:** Database for development, separate for each service.
- **Celery:** Used for scheduling regular tasks to synchronize the Admin API with the Frontend API.
- **Redis:** Acts as a broker for Celery and stores task results.
- **Docker:** Containers to encapsulate environment setup and dependencies for development.

## Getting Started

### Prerequisites

Ensure you have Docker and Docker Compose installed on your system to handle the deployment and management of the containers.

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://your-repository-url.git
cd into folder
```

### Build and Run Containers

Use Docker Compose to build and run the containers for both services:

```bash
docker-compose up --build
```

This command builds the images if they haven't been built and starts the services as configured in `docker-compose.yml`.

### Environment Variables

Adjust the necessary environment variables through the Docker Compose file before building the services. These include:

- `DJANGO_SECRET_KEY`: A secret key for Django.
- `DJANGO_DEBUG`: Debug mode for Django (set to `True` for development).

## Testing

Run tests for each service by accessing their respective containers:

```bash
docker-compose run <service_name> python manage.py test
```

Replace `<service_name>` with `admin_api` or `frontend_api` as required.

---

This README provides a comprehensive overview of your project, how to get it started, and how to interact with it locally. More specific details can be added as the project evolves and moves towards a production deployment.
