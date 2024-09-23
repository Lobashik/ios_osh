import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pictures.settings')
django.setup()

USER = get_user_model()

if not USER.objects.filter(email=os.environ['DJANGO_SUPERUSER_EMAIL']).exists():
    USER.objects.create_superuser(
        email=os.environ['DJANGO_SUPERUSER_EMAIL'],
        username=os.environ['DJANGO_SUPERUSER_USERNAME'],
        password=os.environ['DJANGO_SUPERUSER_PASSWORD']
    )