# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = os.environ.get('DEBUG', True),
ROOT_URLCONF = 'config.urls'
SECRET_KEY = os.environ.get('SECRET_KEY', 'Local development')
WSGI_APPLICATION = 'config.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # third party apps
    'rest_framework',
    # local apps
    'apps',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'app_db'),
        'USER': os.environ.get('APP_USER', 'vagrant'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'vagrant'),
        'HOST': 'localhost',
        'PORT': 5432
    },
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
