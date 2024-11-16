import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CyberHex.settings')

django.setup()

from django.apps import apps

def list_models():
    for app in apps.get_app_configs():
        print(f"App: {app.name}")
        for model in app.get_models():
            print(f"  - Model: {model.__name__}")

list_models()