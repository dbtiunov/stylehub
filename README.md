# StyleHub

StyleHub is a Django web application that allows users to create and manage collections of items. The application consists of a Django backend with templates for the frontend. The main purpose is to display user-created collections and items on the main page.

## Features

- **Authentication and Authorization**
  - Django's built-in authentication system
  - Admin interface for managing content
  - Single user access (admin)

- **Site Settings**
  - Customizable site name
  - Uploadable background image
  - Uploadable logo

- **Collections Management**
  - Create, read, update, delete collections
  - Each collection has a title, slug, and image

- **Collection Items Management**
  - Create, read, update, delete items within collections
  - Each item has a title, URL, image, and link to parent collection

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/stylehub.git
   cd stylehub
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file to set your environment variables:
   - `SECRET_KEY`: A secret key for Django
   - `DEBUG`: Set to `True` for development, `False` for production
   - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
   - `CSRF_TRUSTED_ORIGINS`: Comma-separated list of trusted origins for CSRF
   - `DATABASE_HOST`: PostgreSQL database host (default: localhost)
   - `DATABASE_PORT`: PostgreSQL database port (default: 5432)
   - `DATABASE_NAME`: PostgreSQL database name
   - `DATABASE_USER`: PostgreSQL database user
   - `DATABASE_PASSWORD`: PostgreSQL database password
   - `SUPERUSER_USERNAME`: Default admin username (default: admin)
   - `SUPERUSER_PASSWORD`: Default admin password (default: admin)

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:

   Use the custom management command (uses credentials from .env):
   ```
   python manage.py init_superuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at http://127.0.0.1:8000/

## Usage

1. Log in to the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials.

2. Create site settings:
   - Go to "Site Settings" and add a new entry with your site name, background image, and logo.

3. Create collections:
   - Go to "Collections" and add new collections with titles and images.
   - The slug will be automatically generated from the title if not provided.

4. Add items to collections:
   - You can add items directly from the collection edit page or go to "Collection Items" to add them separately.
   - Each item requires a title, URL, image, and must be linked to a collection.

5. View the collections on the main page at http://127.0.0.1:8000/

6. Click on a collection to view its items.

## Project Structure

- `gallery/` - Main application directory
  - `models.py` - Database models (SiteSettings, Collection, CollectionItem)
  - `views.py` - Views for displaying collections and items
  - `admin.py` - Admin interface configuration
  - `urls.py` - URL patterns for the application

- `templates/gallery/` - HTML templates
  - `base.html` - Base template with common structure and styling
  - `gallery.html` - Template for displaying all collections
  - `collection.html` - Template for displaying a specific collection and its items

- `static/` - Static files (CSS, JavaScript, etc.)
- `media/` - Uploaded media files (images)

## Deployment

The project includes a Procfile for easy deployment to platforms like Heroku. The Procfile automates the following steps:

1. Run database migrations
2. Initialize a default superuser (using credentials from environment variables)
3. Collect static files
4. Start the Gunicorn server

To deploy the application:

1. Set up all required environment variables on your hosting platform
2. Push the code to your hosting platform
3. The application should automatically deploy using the commands in the Procfile

## Dependencies

- Django
- Pillow (for image handling)
- django-cleanup (for automatic file cleanup)
- django-environ (for environment variables management)
- psycopg2 (PostgreSQL database adapter)
- gunicorn (for serving the application in production)
- whitenoise (for serving static files in production)
