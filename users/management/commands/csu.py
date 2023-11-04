from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test1@sky.pro',
            first_name='Test1',
            last_name='Testov1',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password('111')
        user.save()
