from pathlib import Path
import os

SETTINGS_DIR = Path(__file__).resolve().parent          # .../settings
PROJECT_DIR  = SETTINGS_DIR.parent                       # .../friend_ada
SITE_DIR     = PROJECT_DIR.parent                        # .../sites/friend_ada
REPO_ROOT    = SITE_DIR.parent.parent                    # .../web-factory

BASE_DIR = REPO_ROOT  # aby sedel zmysel názvu v projekte

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = [h.strip() for h in os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if h.strip()]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "shared.apps.portfolio",
    "shared.apps.gallery",
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
]

ROOT_URLCONF = "friend_ada.urls"
WSGI_APPLICATION = "friend_ada.wsgi.application"
ASGI_APPLICATION = "friend_ada.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            SITE_DIR / "theme" / "templates",
            REPO_ROOT / "shared" / "core" / "templates_base",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": SITE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "sk"
TIME_ZONE = "Europe/Prague"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [
    REPO_ROOT / "shared" / "core" / "static_base",
    SITE_DIR / "theme" / "static",
]
STATIC_ROOT = STATIC_ROOT = REPO_ROOT / ".staticfiles" / "friend_ada"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = SITE_DIR / ".media"

SITE_BRAND = "Kamarát 1 – osobný web"
