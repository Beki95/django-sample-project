from decouple import config

STATICFILES_STORAGE = config(
    'STATICFILES_STORAGE',
    cast=str,
    default='django.contrib.staticfiles.storage.StaticFilesStorage'
)
STATIC_URL = config(
    'STATIC_URL',
    cast=str,
    default='static/'
)
STATIC_ROOT = config(
    'STATIC_ROOT',
    cast=str,
    default='application/static'
)
