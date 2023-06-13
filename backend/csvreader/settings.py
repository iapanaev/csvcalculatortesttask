import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['ENV'] == 'development'

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'corsheaders',
    'calculator'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
]
    
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

ROOT_URLCONF = 'csvreader.urls'

WSGI_APPLICATION = 'csvreader.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files
STATIC_URL = "static/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


# CORS
CORS_ALLOWED_ORIGINS = os.environ['CORS_ALLOWED_ORIGINS'].split(',')


# Celery settings
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']


# Application specific settings
CSV_FILES_PATH = os.environ['CSV_FILES_PATH']
