"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = os.environ.get(
    "SECRET_KEY", default="hussx3!p=8@%iej1k_7vxd*!6acbv7ln93_+_2ia8kb-becqc1"
)
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", default="127.0.0.1 localhost [::1]"
).split(" ")

CSRF_TRUSTED_ORIGINS = os.environ.get(
    "CSRF_TRUSTED_ORIGINS", default="http://127.0.0.1:8000 http://localhost:8000"
).split(" ")

SESSION_COOKIE_SECURE = True  # ensures cookie is only sent under an HTTPS connection
CSRF_COOKIE_SECURE = True  # ensures CSRF cookie is only sent under an HTTPS connection
SECURE_HSTS_SECONDS = 604800  # determines how long browsers should remember that your site should only be accessed using HTTPS
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)  #  signifies a request is secure despite using proxy
ACCOUNT_DEFAULT_HTTP_PROTOCOL = (
    "https"  # django-allauth's default protocol for generating URLs
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "django_tailwind_cli",
    "theme",
    "django_browser_reload",
    "crispy_forms",
    "crispy_bootstrap4",
    "party",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES["default"] = dj_database_url.config(default="sqlite:///db.sqlite3")


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "theme" / "static_src" / "src",
    BASE_DIR / "party" / "static"
]
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# django-tailwind-cli
# https://django-tailwind-cli.andrich.me/#installation

TAILWIND_CLI_VERSION = "3.4.1"
TAILWIND_CLI_PATH = BASE_DIR / "bin/tailwindcss"
TAILWIND_CLI_AUTOMATIC_DOWNLOAD = False
TAILWIND_CLI_SRC_CSS = BASE_DIR / "theme/static_src/src/styles.css"
TAILWIND_CLI_DIST_CSS = "tailwind.css"
TAILWIND_CLI_CONFIG_FILE = "theme/static_src/tailwind.config.js"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "party.CustomUser"

INTERNAL_IPS = [
    "127.0.0.1",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "page_party_list"  # where to redirect after login
LOGIN_URL = "party_login"  # where to redirect when login is required to access a view


AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

SITE_ID = 1  # needs to match the Site ID in the admin
ACCOUNT_EMAIL_VERIFICATION = "none"  # no email verification needed
SOCIALACCOUNT_LOGIN_ON_GET = True  # skip additional confirm page, less secure
ACCOUNT_LOGOUT_ON_GET = True  # skip the confirm logout page
ACCOUNT_UNIQUE_EMAIL = True
