"""
Django settings for helpdeskdjango project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os, sys


SITE_ID = 1
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Логгирование
# print ("base dir path", BASE_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'formatterNew':{
            'format': '{levelname} {asctime} {process:d} {thread:d} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'firstDebug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'C:/Users/where/Desktop/Профессиональные модули/ПМ 03 Орехов Данил Андреевич/ПП 03.01/Django_Help/helpdeskdjango/deb/debug.log',
            'formatter': 'formatterNew'
        },
    },
    'loggers': {
        'register': {
            'handlers': ['firstDebug'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },

    # 'version': 1,
    # 'disable_existing_loggers': False,
    # 'handlers': {
    #     'console': {
    #         'class': 'logging.StreamHandler',
    #     },
    # },
    # 'root': {
    #     'handlers': ['console'],
    #     'level': 'INFO',
    # },

}


PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$1$$$#8!g@wa^%x!zbdfj^n8c5bl&*i9bh&mgjh%29^evwl7w-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'crispy_forms',
    'import_export',
    'rest_framework', 
    'articles.apps.ArticlesConfig',
    'main.apps.MainConfig',
    'userManual.apps.UsermanualConfig',
    # 'UserProfile.apps.UserprofileConfig',
    'register.apps.RegisterConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    # 'account',
    'ckeditor',
    'ckeditor_uploader',
    'googlecharts',
    # 'debug_toolbar',
    
    
    'allauth',
    # 'allauth.socialaccount.providers.vk'
]

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'account.middleware.LocaleMiddleware',
    # 'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'helpdeskdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            
                # 'account.context_processors.account',
            ],
        },
    },
]

WSGI_APPLICATION = 'helpdeskdjango.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'register.EmailBackend.CustomBackend'

]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_URL="/media_cdn/"
MEDIA_ROOT=os.path.join(BASE_DIR, 'media_cdn')
IMAGES_URL = '/media_cdn/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
# DEFAULT_FROM_EMAIL = 's5mtpev@yandex.ru'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "s5mtpev@yandex.ru"
EMAIL_HOST_PASSWORD = "ECD-xzD-6ui-A2L"
EMAIL_USE_SSL = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {  "default": {  "removePlugins": "stylesheetparser",  } } 

EMAIL_ADMIN = "haevlqgkc.3jm@pxuv.emlhub.com"

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/task_show'

GRAPPELLI_ADMIN_TITLE = 'FCCP HELPDESK'

X_FRAME_OPTIONS = 'ALLOW-FROM https://docs.google.com/forms/'

IMPORT_EXPORT_USE_TRANSACTIONS = True


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


# INTERNAL_IPS = ('127.0.0.1',)

# def show_toolbar(request):
#     return True
# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
# }