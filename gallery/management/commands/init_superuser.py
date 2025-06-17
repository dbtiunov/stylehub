from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=settings.DEFAULT_SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(
                settings.DEFAULT_SUPERUSER_USERNAME,
                password=settings.DEFAULT_SUPERUSER_PASSWORD
            )
            self.stdout.write('Superuser created. You can now log in and change your password.')
        else:
            self.stdout.write('Superuser already exists')
