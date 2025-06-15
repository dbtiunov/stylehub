import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stylehub.settings')

application = get_wsgi_application()

# Use whitenoise to serve static files in production
from whitenoise import WhiteNoise
application = WhiteNoise(application)
