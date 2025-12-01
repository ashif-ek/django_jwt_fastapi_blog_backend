from pathlib import Path
from datetime import timedelta
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    # Render backend hostname
    "https://django-jwt-fastapi-blog-backend-1.onrender.com",
    # Vercel frontend hostname
    "your-frontend-name.vercel.app",
]

# -------------------------------------------------------------------
# APPLICATIONS
# -------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",

    "blog",
]

# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "backend.wsgi.application"

# -------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------

# Use PostgreSQL on Render, SQLite locally
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# STATIC & MEDIA
# -------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# -------------------------------------------------------------------
# DRF / JWT
# -------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# -------------------------------------------------------------------
# CORS
# -------------------------------------------------------------------

CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-name.vercel.app",
]

# For testing only; disable after deploy:
CORS_ALLOW_ALL_ORIGINS = DEBUG

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


















# from pathlib import Path
# from datetime import timedelta
# import os

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = "change-me-to-a-strong-secret-key"
# DEBUG = True
# ALLOWED_HOSTS = ["*"]

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",

#     "rest_framework",
#     "rest_framework.authtoken",
#     "corsheaders",

#     "blog",
# ]

# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware",
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "backend.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "backend.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = "static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"


# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
#     "DEFAULT_PERMISSION_CLASSES": (
#         "rest_framework.permissions.IsAuthenticatedOrReadOnly",
#     ),
# }

# from datetime import timedelta

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "AUTH_HEADER_TYPES": ("Bearer",),
# }

# CORS_ALLOW_ALL_ORIGINS = True
