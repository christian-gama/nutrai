import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') == '1' else False

ALLOWED_HOSTS: list[str] = []

ROOT_URLCONF = 'nutrai.urls'

WSGI_APPLICATION = 'nutrai.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
