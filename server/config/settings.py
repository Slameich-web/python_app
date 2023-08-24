import logging

from pathlib import Path

from environ import Env

import os

env = Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

Env.read_env(BASE_DIR / '.env')

DEBUG = env('DEBUG')

if DEBUG:
    from config.dev import *
else:
    from config.prod import *

SECRET_KEY = env('SECRET_KEY')

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = False
USE_L10N = False

DATETIME_FORMAT = "%d.%m.%Y %H:%M"
SHORT_DATETIME_FORMAT = "%d.%m.%Y %H:%M"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'django_filters',
]

LOCAL_APPS = [
    'core',
]

DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THIRD_PARTY_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

LOCAL_MIDDLEWARE = [

]

INSTALLED_APPS = [*LOCAL_APPS, *THIRD_PARTY_APPS, *DJANGO_APPS]
MIDDLEWARE = [*LOCAL_MIDDLEWARE, *THIRD_PARTY_MIDDLEWARE, *DJANGO_MIDDLEWARE]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 12345,
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%d.%m.%Y %H:%M",
    'EXCEPTION_HANDLER': 'core.utils.typed_exception_handler',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
