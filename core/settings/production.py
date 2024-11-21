from .base import *


env.read_env('.env.production')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))

SECRET_KEY = env.str('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 5432,
    }
}