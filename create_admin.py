import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = "admin"
    email = "hello@anasnc.com"
    password = "adminpass"
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}'...")
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully with password '{password}'!")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == "__main__":
    create_superuser()
