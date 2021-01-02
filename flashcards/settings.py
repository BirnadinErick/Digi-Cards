import os
from datetime import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '4+fdn@cu5n2029x!$of8l=gq_3qy7(yvftk!cia3_1a5u30grk'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'main.apps.MainConfig',
    'markdownx',
    'imagekit',
]

ROOT_URLCONF = 'flashcards.urls'
MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
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

WSGI_APPLICATION = 'flashcards.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flashcards_web',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'birnadin',
        'PASSWORD': 'd3ds3c1am',
    }
}

# Password validation
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

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
#     os.path.join(BASE_DIR, 'home', 'static')
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# MarkdownX settings
MARKDOWNX_MEDIA_PATH = datetime.now().strftime('digi-card-image/%Y/%m/%d')

MARKDOWNX_UPLOAD_MAX_SIZE = 20 * 1024 * 1024  # 20 MB is allowed upload

MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png']

MARKDOWNX_SVG_JAVASCRIPT_PROTECTION = True

MARKDOWNX_EDITOR_RESIZABLE = True

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown_katex',
    'markdown_checklist.extension',
    'markdown_markup_emoji.markup_emoji',
    'MarkdownHighlight.highlight',
    'markdown.extensions.codehilite',
]

MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {
    'markdown.extensions.codehilite': {'use_pygments': True},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
    'markdown_markup_emoji.markup_emoji': {},
}

# Whitenoise settings
WHITENOISE_AUTOREFRESH = True

# # Cache Setting
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:2004',
#     },
#     'frontend': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:2005',
#
#     }
# }

# htmlmin settings
# HTML_MINIFY = True
