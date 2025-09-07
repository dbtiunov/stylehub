# syntax=docker/dockerfile:1
FROM python:3.12-slim

# System deps for psycopg2 and building wheels
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libpq-dev \
       netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (leverage Docker cache)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create non-root user
RUN useradd -m appuser \
    && mkdir -p /app/staticfiles /app/media \
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Healthcheck (optional basic TCP check)
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s CMD nc -z 127.0.0.1 8000 || exit 1

# Start the app similar to Procfile: migrate, init superuser, collectstatic, then gunicorn
CMD sh -c "python manage.py migrate \
           && python manage.py init_superuser \
           && python manage.py collectstatic --noinput \
           && gunicorn -b 0.0.0.0:8000 stylehub.wsgi:application"
