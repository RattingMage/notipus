"""
Django settings for django_notipus project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from webhooks.services.event_processor import EventProcessor
from webhooks.providers.chargify import ChargifyProvider
from webhooks.providers.shopify import ShopifyProvider
from webhooks.providers.stripe import StripeProvider

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))  # Load variables from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_DJANGO_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", False)

APP_NAME = os.environ.get("FLY_APP_NAME")
# ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "webhooks",
    "core",
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

ROOT_URLCONF = "django_notipus.urls"

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

WSGI_APPLICATION = "django_notipus.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"

# Specify the directory where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Specify additional directories for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "webhooks": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}


CHARGIFY_WEBHOOK_SECRET = os.getenv("CHARGIFY_WEBHOOK_SECRET")


# Provider configurations
SHOPIFY_SHOP_URL = os.getenv("SHOPIFY_SHOP_URL")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_WEBHOOK_SECRET = os.getenv("SHOPIFY_WEBHOOK_SECRET")
SHOPIFY_PROVIDER = ShopifyProvider(webhook_secret=SHOPIFY_WEBHOOK_SECRET)

CHARGIFY_PROVIDER = ChargifyProvider(webhook_secret="your_chargify_webhook_secret")

# Event processor configuration
EVENT_PROCESSOR = EventProcessor()

# Slack client configuration
# SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SLACK_CLIENT = None

SLACK_CLIENT_ID = os.getenv("SLACK_CLIENT_ID")
SLACK_CLIENT_SECRET = os.getenv("SLACK_CLIENT_SECRET")
SLACK_REDIRECT_URI = os.getenv("SLACK_REDIRECT_URI")

SLACK_CLIENT_BOT_ID = os.getenv("SLACK_CLIENT_BOT_ID")
SLACK_CLIENT_BOT_SECRET = os.getenv("SLACK_CLIENT_BOT_SECRET")
SLACK_REDIRECT_BOT_URI = os.getenv("SLACK_REDIRECT_BOT_URI")

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
STRIPE_PLANS = {
    "basic": os.getenv("STRIPE_BASIC_PLAN"),
    "pro": os.getenv("STRIPE_PRO_PLAN"),
    "enterprise": os.getenv("STRIPE_ENTERPRISE_PLAN"),
}
TRIAL_PERIOD_DAYS = 14
STRIPE_PROVIDER = StripeProvider(STRIPE_WEBHOOK_SECRET)

DISABLE_BILLING = os.getenv("DISABLE_BILLING", "False").lower() == "true"
