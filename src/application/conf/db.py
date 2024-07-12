from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB', cast=str),
        'USER': config('POSTGRES_USER', cast=str),
        'PASSWORD': config('POSTGRES_PASSWORD', cast=str),
        'HOST': config('POSTGRES_HOST', cast=str),
        'PORT': config('POSTGRES_PORT', cast=int),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
