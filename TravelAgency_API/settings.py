import os
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2jz4h_#35psowa*h(ofq%@%9q98syy8v!rw$_+s3=es-i^%z1s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'ta-travel-agency-api-1bae69c42c2d.herokuapp.com',
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'travel_api.apps.TravelApiConfig',
    'django_filters',
    'rest_framework',
    'modeltranslation',
    'corsheaders',
    'rest_framework_jwt',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DATETIME_FORMAT': '%Y-%m-%d',
    'ORDERING_PARAM': 'sort',
    'EXCEPTION_HANDLER': 'travel_api.utils.custom_exception_handler',
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = "TravelAgency_API.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "TravelAgency_API.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'd5GoRJdiCvx1FU9wPqvq',
        'HOST': 'containers-us-west-119.railway.app',
        'PORT': '7423',
    }
}

LIQPAY_PUBLIC_KEY = 'sandbox_i19318155047'
LIQPAY_PRIVATE_KEY = 'sandbox_fO53arKOsERqttKl5RWMEohhDUJbvFxCyEy062iD'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization

LANGUAGE_CODE = 'uk'

LANGUAGES = [
    ('uk', 'Ukrainian'),
    ('ru', 'Russian'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'uk'
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': ('uk', 'ru'),
    'uk': ('uk', 'ru'),
    'ru': ('ru', 'uk'),
}


TIME_ZONE = "Europe/Kiev"

DATE_INPUT_FORMATS = ['%d-%m-%Y']

USE_I18N = True

USE_TZ = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATIC_URL = "static/"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ivmitqa@gmail.com'
EMAIL_HOST_PASSWORD = 'hkjo icdy bewp kuoo'
EMAIL_ADMIN_RECIPIENT = "adm.ivm.it@gmail.com"

BASE_URL = 'http://127.0.0.1:8000'
