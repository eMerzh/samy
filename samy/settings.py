"""
Django settings for samy project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = True
try:
    os.environ['DEV']
    DEBUG = True
    # MEDIA_ROOT = './static/media/'
    # MEDIA_URL = 'media/'
    # STATIC_ROOT = './static/'
    STATIC_URL = 'static/'
except KeyError:
    MEDIA_ROOT = './static/media/'
    MEDIA_URL = 'media/'
    STATIC_ROOT = './static/'
    STATIC_URL = 'static/'
    DEBUG = False

CSRF_COOKIE_HTTPONLY = True

try:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.55', os.environ['HOST']]
except:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.55']

DJANGO_SUPERUSER_USERNAME = os.environ['DJANGO_SUPERUSER_USERNAME']
DJANGO_SUPERUSER_PASSWORD = os.environ['DJANGO_SUPERUSER_PASSWORD']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    # 'api.apps.ApiConfig',
    'api',
    'storages',
    'django_filters'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Note that this needs to be placed above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ]
}

AUTH_USER_MODEL = 'api.CustomUser'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://192.168.0.55:3000',
    'http://192.168.0.55:8000'
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'samy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'samy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587  # TLS
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 10
try:
    EMAIL_HOST_USER = os.environ['SMTP_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
except KeyError:
    raise EnvironmentError('Email variables are not defined.')

# MySQL


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'samy',
        'HOST': '127.0.0.1',
        'PORT': '3307',
        'USER': 'root',
        'PASSWORD': 'plumeplume',
        'CHARSET': 'utf8'
    }
}

try:
    DATABASES['default']['HOST'] = os.environ['MYSQL_HOST']
except KeyError:
    print('MySql DB host is not present in the environment.')
try:
    DATABASES['default']['PORT'] = os.environ['MYSQL_PORT']
except KeyError:
    print('MySql DB port is not present in the environment.')
try:
    DATABASES['default']['USER'] = os.environ['MYSQL_USER']
except KeyError:
    print('MySql DB user is not present in the environment.')
try:
    DATABASES['default']['PASSWORD'] = os.environ['MYSQL_PASSWORD']
except KeyError:
    print('MySql DB password is not present in the environment.')
try:
    DATABASES['default']['NAME'] = os.environ['MYSQL_DBNAME']
except KeyError:
    print('MySql DB NAME is not present in the environment.')

# S3 FILE storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
AWS_QUERYSTRING_AUTH = False
# AWS_QUERYSTRING_EXPIRE = 10 * 365 * 24 * 60 * 60
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_DEFAULT_ACL = 'public-read'
