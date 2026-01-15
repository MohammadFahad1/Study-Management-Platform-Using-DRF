# Study Management Platform

A Django-based web application for managing study materials such as flashcards, quizzes and matching games.

## API Endpoint Documentation

The API endpoint documentation can be accessed from the [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) link after installation.

## Setup

1. Clone the repository: `git clone https://github.com/fahadbd/study-management-platform.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a new database: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`

## Environment Variables

The following environment variables are required to run the application:

- `EMAIL_HOST`: The SMTP server to use for sending emails.
- `EMAIL_USE_TLS`: Whether to use TLS when sending emails.
- `EMAIL_PORT`: The port to use when sending emails.
- `EMAIL_HOST_USER`: The username to use when sending emails.
- `EMAIL_HOST_PASSWORD`: The password to use when sending emails.

Example:
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=your_email_here
EMAIL_HOST_PASSWORD=password_here
