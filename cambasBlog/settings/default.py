import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, '../')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
LOCAL = os.environ.get('LOCAL', 'False').lower() == 'true'
TESTING_MODE = 'test' in sys.argv
DEV_MODE = DEBUG and not TESTING_MODE
SHOW_DEBUG_TOOLBAR = DEV_MODE and os.environ.get(
    'SHOW_DEBUG_TOOLBAR', 'False').lower() == 'true'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'versatileimagefield',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'djcelery_email',

    'cambasBlog.apps.core',
    'cambasBlog.apps.users',
    'cambasBlog.apps.messaging.email',
    'cambasBlog.apps.blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'cambasBlog.wsgi.application'
ROOT_URLCONF = 'cambasBlog.urls'
AUTH_USER_MODEL = 'cambasBlog_users.User'
SITE_ID = 1
