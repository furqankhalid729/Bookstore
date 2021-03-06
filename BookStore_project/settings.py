"""
Django settings for BookStore_project project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import ENVIRONMENT as ENVIRONMENT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rqd&9bg=ao7tj9yi3^d2@lj%1bi3*i20agxj+o%5d9*max5bu5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['bookstore729.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'debug_toolbar',
    'whitenoise.runserver_nostatic',
    'allauth',
    'allauth.account',
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'orders.apps.OrdersConfig',

    'Bookes.apps.BookesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'BookStore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'BookStore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'postgres',
        'USER':'postgres',
        'PASSWORD':'12345',
         'HOST':'localhost',
        'POST':5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


AUTH_USER_MODEL='users.customeruser'
LOGIN_REDIRECT_URL='home'
LOGOUT_REDIRECT_URL='home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID=1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', # new
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new

ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_UNIQUE=True
ACCOUNT_AUTHENTICATION_METHOD='email'


DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'
STRIPE_TEST_PUBLISHABLE_KEY='pk_test_51H9l8nEQL3aC4YlHcUz6qqtgq80RGYHfQNtAwieaFZEzQdnL9XdcTXWnpoSEGmwtsYzLFjjnjHvVik75ytfQ8MKK00tnVNDtlJ'
STRIPE_TEST_SECRET_KEY='sk_test_51H9l8nEQL3aC4YlHithd8NQRBMsxtffTdEYG4BGOcZCnCxMsQBYIYQoVFpSKoBeyR19U4ABjLQw9NleN7QGALwp600GHcVMSQw'
INTERNAL_IPS = ('127.0.0.1', )


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
