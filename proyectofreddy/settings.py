import os
from pathlib import Path
import dj_database_url
from decouple import config

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-unsafe")

# DEBUG
DEBUG = os.environ.get("DEBUG", "False") == "True"

# ALLOWED HOSTS
ALLOWED_HOSTS = [
    "bitraptorlabs.com",        # tu dominio propio
    "www.bitraptorlabs.com",    # si usas el www
    "proyecto-bit-raptors-laps.onrender.com",  # el dominio de Render
    "localhost", "127.0.0.1"    # opcional para pruebas locales
]

# CSRF (agrega aquí tu dominio propio y el de Render)
CSRF_TRUSTED_ORIGINS = [
    "https://bitraptorlabs.com",
    "https://www.bitraptorlabs.com",
    "proyecto-bit-raptors-laps.onrender.com",  # dominio en Render
]

# INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # tus apps
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT URL
ROOT_URLCONF = 'proyectofreddy.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "Templates"],  # Ajusta si usas carpeta templates
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

# WSGI
WSGI_APPLICATION = 'proyectofreddy.wsgi.application'

# DATABASE (Render usa DATABASE_URL automáticamente)
DATABASES = {
    'default': dj_database_url.config(
        default="postgresql://postgres:postgres@localhost:5432/postgres",
        conn_max_age=600,
        ssl_require=True
    )
}

# PASSWORDS
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

# LANGUAGE
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "Public"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# DEFAULT PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
