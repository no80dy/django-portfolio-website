import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
SECRET_KEY = os.environ.get('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',

    'crispy_forms',
    'crispy_bootstrap4',
    'django_filters',
    'ckeditor',
    'ckeditor_uploader',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nobodyas.urls'

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

WSGI_APPLICATION = 'nobodyas.wsgi.application'

_PASS = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{_PASS}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{_PASS}.MinimumLengthValidator',
    },
    {
        'NAME': f'{_PASS}.CommonPasswordValidator',
    },
    {
        'NAME': f'{_PASS}.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_RECEIVER = os.environ.get('EMAIL_HOST_RECEIVER')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%'
    }
}
