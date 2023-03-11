import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = Path(__file__).resolve().parent

SECRET_KEY = "django-insecure-$^tmpl8k*_07yyvpo7k^r2=wlu87hd@*@!)c6kdr&lz5vm7djb"

DEBUG = True

ALLOWED_HOSTS: list[str] = ["localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "app.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": f"{PROJECT_DIR}/{os.getenv('DATABASE_NAME')}.db",
#     }
# }

DATABASES = {
    'default': {

        'ENGINE': os.getenv('DATABASE_ENGINE'),

        'NAME': os.getenv('DATABASE_NAME'),

        'USER': os.getenv('DATABASE_USER'),

        'PASSWORD': os.getenv('DATABASE_PASS'),

        'HOST': os.getenv('DATABASE_HOST'),

        'PORT': os.getenv('DATABASE_PORT'),

    }
}

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

LANGUAGE_CODE = "fr"

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = PROJECT_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
