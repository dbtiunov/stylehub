web: python manage.py migrate
     && python manage.py init_superuser
     && python manage.py collectstatic --noinput
     && gunicorn -b 0.0.0.0:8000 stylehub.wsgi:application
