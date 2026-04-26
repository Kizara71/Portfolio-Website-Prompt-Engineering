import os
import django

# Setup the Django environment before importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.environ.get('ADMIN_USERNAME')
    password = os.environ.get('ADMIN_PASSWORD')
    email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

    if username and password:
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser: {username}")
            User.objects.create_superuser(username=username, email=email, password=password)
            print("Superuser created successfully.")
        else:
            print(f"Superuser '{username}' already exists. Skipping creation.")
    else:
        print("ADMIN_USERNAME or ADMIN_PASSWORD not found in environment variables. Skipping superuser creation.")

if __name__ == '__main__':
    create_superuser()
